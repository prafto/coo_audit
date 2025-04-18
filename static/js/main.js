// DOM Elements
const caseIdForm = document.getElementById('caseIdForm');
const caseIdInput = document.getElementById('caseId');
const loadingSpinner = document.getElementById('loadingSpinner');
const errorMessage = document.getElementById('errorMessage');
const resultsSection = document.getElementById('results');
const cooSection = document.getElementById('cooSection');

// Chart instance
let sentimentChart = null;

// Event Listeners
document.addEventListener('DOMContentLoaded', () => {
    caseIdForm.addEventListener('submit', handleFormSubmit);
});

// Form Submission Handler
async function handleFormSubmit(event) {
    event.preventDefault();
    
    const caseId = caseIdInput.value.trim();
    const storeId = document.getElementById('storeId').value.trim();
    
    if (!caseId || !storeId) {
        showError('Please enter valid case ID and store ID');
        return;
    }
    
    // Show loading state
    loadingSpinner.classList.remove('d-none');
    errorMessage.classList.add('d-none');
    resultsSection.classList.add('d-none');
    cooSection.classList.add('d-none');
    
    try {
        const response = await fetch('/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                case_number: caseId,
                store_id: storeId
            }),
        });
        
        if (!response.ok) {
            throw new Error('Failed to analyze case');
        }
        
        const data = await response.json();
        displayResults(data);
    } catch (error) {
        showError(error.message);
    } finally {
        loadingSpinner.classList.add('d-none');
    }
}

// Display Results
function displayResults(data) {
    // Update summary statistics
    document.getElementById('totalEmails').textContent = data.total_emails || 0;
    document.getElementById('supportEmails').textContent = data.support_emails || 0;
    document.getElementById('merchantEmails').textContent = data.merchant_emails || 0;
    
    // Update sentiment meter
    const sentimentScore = data.average_sentiment_score || 0;
    const sentimentMeter = document.getElementById('sentimentMeter');
    const sentimentScoreElement = document.getElementById('sentimentScore');
    
    // Set the width of the progress bar (from -1 to 1)
    const percentage = ((sentimentScore + 1) / 2) * 100; // Convert from [-1, 1] to [0, 100]
    sentimentMeter.style.width = `${percentage}%`;
    sentimentMeter.setAttribute('aria-valuenow', sentimentScore);
    
    // Update the displayed score
    sentimentScoreElement.textContent = sentimentScore.toFixed(2);
    
    // Set the color based on sentiment score using a consistent gradient
    if (sentimentScore < -0.3) {
        sentimentMeter.classList.remove('bg-success', 'bg-warning');
        sentimentMeter.classList.add('bg-danger');
    } else if (sentimentScore > 0.3) {
        sentimentMeter.classList.remove('bg-danger', 'bg-warning');
        sentimentMeter.classList.add('bg-success');
    } else {
        sentimentMeter.classList.remove('bg-danger', 'bg-success');
        sentimentMeter.classList.add('bg-warning');
    }
    
    // Update sentiment chart
    updateSentimentChart(data.sentiment_timeline || []);
    
    // Update email conversation
    updateEmailConversation(data.processed_emails || []);
    
    // Always show COO section and update with available data
    cooSection.classList.remove('d-none');
    updateCOOInformation(data.coo_data || {});
    
    // Show results section
    resultsSection.classList.remove('d-none');
}

// Helper function to get sentiment color based on score
function getSentimentColor(score) {
    // Round to nearest 0.1 to match our color map
    const roundedScore = Math.round(score * 10) / 10;
    
    // Hardcoded color map for each 0.1 increment from -1.0 to 1.0
    const colorMap = {
        '-1.0': 'rgb(139, 0, 0)',      // Dark red
        '-0.9': 'rgb(160, 0, 0)',      // Slightly less dark red
        '-0.8': 'rgb(180, 0, 0)',      // Even less dark red
        '-0.7': 'rgb(200, 0, 0)',      // Medium dark red
        '-0.6': 'rgb(220, 0, 0)',      // Lighter dark red
        '-0.5': 'rgb(240, 0, 0)',      // Very light dark red
        '-0.4': 'rgb(255, 51, 0)',     // Red with a hint of orange
        '-0.3': 'rgb(255, 102, 0)',    // More orange-red
        '-0.2': 'rgb(255, 153, 0)',    // Orange with a hint of red
        '-0.1': 'rgb(255, 204, 0)',    // Orange-yellow
        '0.0': 'rgb(255, 255, 0)',     // Yellow
        '0.1': 'rgb(204, 255, 0)',     // Yellow with a hint of green
        '0.2': 'rgb(153, 255, 0)',     // More green-yellow
        '0.3': 'rgb(102, 255, 0)',     // Even more green-yellow
        '0.4': 'rgb(51, 255, 0)',      // Mostly green with a hint of yellow
        '0.5': 'rgb(0, 255, 0)',       // Pure green
        '0.6': 'rgb(0, 230, 0)',       // Slightly darker green
        '0.7': 'rgb(0, 204, 0)',       // More darker green
        '0.8': 'rgb(0, 179, 0)',       // Even darker green
        '0.9': 'rgb(0, 153, 0)',       // Very dark green
        '1.0': 'rgb(0, 128, 0)'        // Darkest green
    };
    
    // Return the color from the map, or default to yellow if not found
    return colorMap[roundedScore.toString()] || 'rgb(255, 255, 0)';
}

// Update Sentiment Chart
function updateSentimentChart(sentimentTimeline) {
    const ctx = document.getElementById('sentimentChart').getContext('2d');
    
    // Destroy existing chart if it exists
    if (sentimentChart) {
        sentimentChart.destroy();
    }
    
    // Sort the sentiment timeline by date (earliest to latest)
    const sortedTimeline = [...sentimentTimeline].sort((a, b) => {
        return new Date(a.timestamp) - new Date(b.timestamp);
    });
    
    // Extract dates and scores from the sorted timeline
    const dates = sortedTimeline.map(item => new Date(item.timestamp).toLocaleString());
    const scores = sortedTimeline.map(item => item.sentiment_score);
    
    // Create the chart
    sentimentChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{
                label: 'Sentiment Score',
                data: scores,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1,
                fill: false
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false, // Allow the chart to be as tall as needed
            scales: {
                y: {
                    beginAtZero: true,
                    min: -1,
                    max: 1,
                    title: {
                        display: true,
                        text: 'Sentiment Score'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Time'
                    }
                }
            },
            plugins: {
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const index = context.dataIndex;
                            const item = sortedTimeline[index];
                            return [
                                `Score: ${item.sentiment_score.toFixed(2)}`,
                                `Category: ${item.category}`,
                                `Details: ${item.details.explanation}`
                            ];
                        }
                    }
                }
            }
        }
    });
}

// Update Email Conversation
function updateEmailConversation(emails) {
    const conversationContainer = document.getElementById('emailConversation');
    conversationContainer.innerHTML = '';
    
    if (emails.length === 0) {
        conversationContainer.innerHTML = '<p class="text-center">No emails found.</p>';
        return;
    }
    
    // Sort emails by timestamp
    emails.sort((a, b) => new Date(a.timestamp) - new Date(b.timestamp));
    
    // Create accordion items for each email
    emails.forEach((email, index) => {
        const accordionItem = document.createElement('div');
        accordionItem.className = 'accordion-item';
        
        const headerId = `heading${index}`;
        const collapseId = `collapse${index}`;
        
        const timestamp = new Date(email.timestamp).toLocaleString();
        const sentimentClass = email.sentiment_score < -0.3 ? 'text-danger' : 
                             email.sentiment_score > 0.3 ? 'text-success' : 'text-warning';
        
        accordionItem.innerHTML = `
            <h2 class="accordion-header" id="${headerId}">
                <button class="accordion-button ${index === 0 ? '' : 'collapsed'}" type="button" 
                        data-bs-toggle="collapse" data-bs-target="#${collapseId}" 
                        aria-expanded="${index === 0 ? 'true' : 'false'}" 
                        aria-controls="${collapseId}">
                    <div class="d-flex justify-content-between align-items-center w-100">
                        <span>${timestamp}</span>
                        <span class="${sentimentClass} ms-2">
                            Sentiment: ${email.sentiment_score.toFixed(2)}
                        </span>
                    </div>
                </button>
            </h2>
            <div id="${collapseId}" class="accordion-collapse collapse ${index === 0 ? 'show' : ''}" 
                 aria-labelledby="${headerId}" data-bs-parent="#emailConversation">
                <div class="accordion-body">
                    <p><strong>From:</strong> ${email.from}</p>
                    <p><strong>To:</strong> ${email.to}</p>
                    <p><strong>Subject:</strong> ${email.subject}</p>
                    <hr>
                    <div class="email-content">${email.content}</div>
                </div>
            </div>
        `;
        
        conversationContainer.appendChild(accordionItem);
    });
}

// Update COO Information
function updateCOOInformation(cooData) {
    // Update store information
    document.getElementById('cooStoreId').textContent = cooData.store_id || 'N/A';
    document.getElementById('cooStoreName').textContent = cooData.store_name || 'N/A';
    document.getElementById('cooBusinessId').textContent = cooData.business_id || 'N/A';
    document.getElementById('cooLegalBusinessName').textContent = cooData.legal_business_name || 'N/A';
    
    // Update new owner information
    document.getElementById('cooNewOwnerName').textContent = 
        `${cooData.new_owner_first_name || ''} ${cooData.new_owner_last_name || ''}`.trim() || 'N/A';
    document.getElementById('cooNewOwnerEmail').textContent = cooData.new_owner_email || 'N/A';
    document.getElementById('cooNewOwnerPhone').textContent = cooData.new_owner_phone || 'N/A';
    
    // Update COO process timeline
    document.getElementById('cooProcessStarted').textContent = 
        cooData.process_started_at ? new Date(cooData.process_started_at).toLocaleString() : 'N/A';
    document.getElementById('cooProcessEnded').textContent = 
        cooData.process_ended_at ? new Date(cooData.process_ended_at).toLocaleString() : 'N/A';
    document.getElementById('cooDuration').textContent = cooData.duration || 'N/A';
    document.getElementById('cooScheduledCutoffTime').textContent = 
        cooData.scheduled_cutoff_time ? new Date(cooData.scheduled_cutoff_time).toLocaleString() : 'N/A';
    
    // Update status information
    document.getElementById('cooApprovalStatus').textContent = cooData.approval_status || 'N/A';
    document.getElementById('cooOnboardingStatus').textContent = cooData.onboarding_status || 'N/A';
    document.getElementById('cooApprovedAt').textContent = 
        cooData.approved_at ? new Date(cooData.approved_at).toLocaleString() : 'N/A';
    document.getElementById('cooCancelledAt').textContent = 
        cooData.cancelled_at ? new Date(cooData.cancelled_at).toLocaleString() : 'N/A';
    
    // Update additional information
    document.getElementById('cooRevokeAccess').textContent = cooData.revoke_access ? 'Yes' : 'No';
    document.getElementById('cooCreateNewBusiness').textContent = cooData.create_new_business ? 'Yes' : 'No';
    document.getElementById('cooPaymentAccountId').textContent = cooData.payment_account_id || 'N/A';
    document.getElementById('cooPactsafeActivityId').textContent = cooData.pactsafe_activity_id || 'N/A';
    
    // Update COO events
    const cooEvents = document.getElementById('cooEvents');
    cooEvents.innerHTML = '';
    
    if (cooData.events && cooData.events.length > 0) {
        cooData.events.forEach(event => {
            const eventElement = document.createElement('div');
            eventElement.className = 'coo-event';
            
            const timestamp = new Date(event.timestamp).toLocaleString();
            
            eventElement.innerHTML = `
                <span class="coo-event-time">${timestamp}</span>
                <p class="mb-0">${event.description}</p>
            `;
            
            cooEvents.appendChild(eventElement);
        });
    } else {
        cooEvents.innerHTML = '<p>No events found.</p>';
    }
}

// Show Error Message
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.remove('d-none');
} 