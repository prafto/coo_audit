// DOM Elements
const caseIdForm = document.getElementById('caseIdForm');
const caseIdInput = document.getElementById('caseId');
const loadingSpinner = document.getElementById('loadingSpinner');
const errorMessage = document.getElementById('errorMessage');
const resultsSection = document.getElementById('results');

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
        showError('Please enter both case number and store number');
        return;
    }
    
    // Show loading state
    loadingSpinner.classList.remove('d-none');
    errorMessage.classList.add('d-none');
    resultsSection.classList.add('d-none');
    
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
        displayCOOInfo(data.coo_info);
    } catch (error) {
        showError(error.message);
    } finally {
        loadingSpinner.classList.add('d-none');
    }
}

// Display Results
function displayResults(data) {
    // Update summary statistics
    document.getElementById('totalEmails').textContent = data.total_emails;
    document.getElementById('supportEmails').textContent = data.support_emails;
    document.getElementById('merchantEmails').textContent = data.merchant_emails;
    
    // Update sentiment meter
    const sentimentScore = data.avg_sentiment;
    const sentimentMeter = document.getElementById('sentimentMeter');
    const sentimentScoreElement = document.getElementById('sentimentScore');
    
    // Set the width of the progress bar (from -1 to 1)
    sentimentMeter.style.width = `${(sentimentScore + 1) * 50}%`;
    sentimentMeter.setAttribute('aria-valuenow', sentimentScore);
    
    // Update the displayed score
    sentimentScoreElement.textContent = sentimentScore.toFixed(2);
    
    // Set the color based on sentiment score using a consistent gradient
    sentimentMeter.style.backgroundColor = getSentimentColor(sentimentScore);
    
    // Update sentiment chart
    updateSentimentChart(data.sentiment_timeline);
    
    // Update email conversation
    updateEmailConversation(data.emails);
    
    // Show results section
    resultsSection.classList.remove('d-none');
}

// Display COO Information
function displayCOOInfo(cooInfo) {
    const cooSection = document.getElementById('cooInfo');
    if (!cooInfo) {
        cooSection.classList.add('d-none');
        return;
    }

    // Update COO information fields
    document.getElementById('cooStoreId').textContent = cooInfo.store_id || '-';
    document.getElementById('cooStoreName').textContent = cooInfo.store_name || '-';
    document.getElementById('cooNewOwnerName').textContent = cooInfo.new_owner_name || '-';
    document.getElementById('cooNewOwnerEmail').textContent = cooInfo.new_owner_email || '-';
    document.getElementById('cooStatus').textContent = cooInfo.coo_status || '-';
    document.getElementById('cooApprovedAt').textContent = cooInfo.approved_at || '-';
    document.getElementById('cooApprovalStatus').textContent = cooInfo.approval_status || '-';
    document.getElementById('cooOnboardingStatus').textContent = cooInfo.onboarding_status || '-';

    // Show the COO section
    cooSection.classList.remove('d-none');
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
        return new Date(a.date) - new Date(b.date);
    });
    
    // Extract dates and scores from the sorted timeline
    const dates = sortedTimeline.map(item => item.date);
    const scores = sortedTimeline.map(item => item.score);
    
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
                        text: 'Date'
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
                                `Score: ${item.score.toFixed(2)}`,
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
    
    // No need to filter since we're only receiving merchant emails from the backend
    emails.forEach((email, index) => {
        const emailItem = document.createElement('div');
        emailItem.className = 'accordion-item';
        
        // Format the date
        const emailDate = new Date(email.date).toLocaleString();
        
        // Determine the email class and sentiment color based on sentiment score
        let emailClass = '';
        let sentimentColor = '#6c757d'; // Default gray for neutral
        
        if (email.sentiment_score !== undefined) {
            // Always use the getSentimentColor function for consistent coloring
            sentimentColor = getSentimentColor(email.sentiment_score);
            
            if (email.sentiment_score > 0.5) {
                emailClass = 'positive-sentiment';
            } else if (email.sentiment_score < -0.5) {
                emailClass = 'negative-sentiment';
            } else {
                emailClass = 'neutral-sentiment';
            }
        }
        
        // Create email header with sender, date, and sentiment circle
        const emailHeader = `
            <div class="d-flex justify-content-between align-items-center">
                <div class="d-flex align-items-center">
                    <div class="sentiment-circle me-2" style="background-color: ${sentimentColor};"></div>
                    <span class="fw-bold">${email.from || 'Unknown sender'}</span>
                </div>
                <div class="date-badge bg-light text-dark px-3 py-1 rounded">
                    <small class="fw-bold">${emailDate}</small>
                </div>
            </div>
        `;
        
        // Create sentiment information if available
        let sentimentInfo = '';
        if (email.sentiment_score !== undefined) {
            sentimentInfo = `
                <div class="sentiment-info mt-2" style="border-left: 4px solid ${sentimentColor}; padding-left: 10px;">
                    <p><strong>Sentiment:</strong> ${email.sentiment_category} (${email.sentiment_score.toFixed(2)})</p>
                </div>
            `;
            
            // Add noteworthy snippets if available
            if (email.noteworthy_snippets && email.noteworthy_snippets.length > 0) {
                sentimentInfo += `
                    <div class="mt-2">
                        <strong>Noteworthy Snippets:</strong>
                        <ul>
                            ${email.noteworthy_snippets.map(snippet => `<li>${snippet}</li>`).join('')}
                        </ul>
                    </div>
                `;
            }
        }
        
        // Create collapsible email content
        const emailContent = `
            <div class="email-content mt-3">
                <p><strong>Subject:</strong> ${email.subject || 'No subject'}</p>
                <div class="email-text">
                    ${email.text.replace(/\n/g, '<br>')}
                </div>
            </div>
        `;
        
        // Create the accordion item
        emailItem.innerHTML = `
            <h2 class="accordion-header">
                <button class="accordion-button ${index === 0 ? '' : 'collapsed'}" type="button" data-bs-toggle="collapse" data-bs-target="#email${index}">
                    ${emailHeader}
                </button>
            </h2>
            <div id="email${index}" class="accordion-collapse collapse ${index === 0 ? 'show' : ''}" data-bs-parent="#emailConversation">
                <div class="accordion-body ${emailClass}">
                    ${sentimentInfo}
                    <div class="d-flex justify-content-start mt-3">
                        <button class="btn btn-sm btn-outline-secondary show-content" data-target="content${index}">
                            Show Email Content
                        </button>
                    </div>
                    <div id="content${index}" class="email-content-container d-none">
                        ${emailContent}
                    </div>
                </div>
            </div>
        `;
        
        conversationContainer.appendChild(emailItem);
    });
    
    // Add event listeners to show/hide buttons
    document.querySelectorAll('.show-content').forEach(button => {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const contentContainer = document.getElementById(targetId);
            contentContainer.classList.toggle('d-none');
            this.textContent = contentContainer.classList.contains('d-none') ? 
                'Show Email Content' : 'Hide Email Content';
        });
    });
}

// Show Error Message
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.remove('d-none');
} 