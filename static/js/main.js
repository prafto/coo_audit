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
    if (!caseId) {
        showError('Please enter a valid case ID');
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
            body: JSON.stringify({ case_number: caseId }),
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
    document.getElementById('totalEmails').textContent = data.total_emails;
    document.getElementById('supportEmails').textContent = data.support_emails;
    document.getElementById('merchantEmails').textContent = data.merchant_emails;
    
    // Update sentiment meter
    const sentimentScore = data.avg_sentiment;
    const sentimentMeter = document.getElementById('sentimentMeter');
    sentimentMeter.style.width = `${(sentimentScore + 1) * 50}%`;
    sentimentMeter.setAttribute('aria-valuenow', sentimentScore);
    
    // Update sentiment chart
    updateSentimentChart(data.sentiment_timeline);
    
    // Update email conversation
    updateEmailConversation(data.emails);
    
    // Show results section
    resultsSection.classList.remove('d-none');
}

// Update Sentiment Chart
function updateSentimentChart(timeline) {
    const ctx = document.getElementById('sentimentChart').getContext('2d');
    
    // Destroy existing chart if it exists
    if (sentimentChart) {
        sentimentChart.destroy();
    }
    
    // Create new chart
    sentimentChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: timeline.map(item => {
                // Parse the date string from the backend
                const date = new Date(item.date);
                return date.toLocaleDateString();
            }),
            datasets: [{
                label: 'Sentiment Score',
                data: timeline.map(item => item.score),
                borderColor: '#0d6efd',
                backgroundColor: 'rgba(13, 110, 253, 0.1)',
                tension: 0.4,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    min: -1,
                    max: 1,
                    ticks: {
                        stepSize: 0.5
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}

// Update Email Conversation
function updateEmailConversation(emails) {
    const conversationContainer = document.getElementById('emailConversation');
    conversationContainer.innerHTML = '';
    
    emails.forEach((email, index) => {
        const emailItem = document.createElement('div');
        emailItem.className = 'accordion-item';
        
        // Determine if it's a support or merchant email
        const isSupport = email.is_support;
        const emailClass = isSupport ? 'support-email' : 'merchant-email';
        
        // Format the date
        const emailDate = email.date ? new Date(email.date).toLocaleString() : 'Unknown date';
        
        // Create the email content
        let emailContent = `<div class="email-content">${email.body || 'No content'}</div>`;
        
        // Add sentiment information for merchant emails
        if (!isSupport && email.sentiment_category) {
            emailContent += `
                <div class="mt-3">
                    <strong>Sentiment:</strong> ${email.sentiment_category}
                    <br>
                    <small class="text-muted">Score: ${email.sentiment_score.toFixed(2)}</small>
                </div>
            `;
            
            // Add noteworthy snippets if available
            if (email.noteworthy_snippets && email.noteworthy_snippets.length > 0) {
                emailContent += `
                    <div class="mt-2">
                        <strong>Noteworthy Snippets:</strong>
                        <ul>
                            ${email.noteworthy_snippets.map(snippet => `<li>${snippet}</li>`).join('')}
                        </ul>
                    </div>
                `;
            }
        }
        
        emailItem.innerHTML = `
            <h2 class="accordion-header">
                <button class="accordion-button ${index === 0 ? '' : 'collapsed'}" type="button" data-bs-toggle="collapse" data-bs-target="#email${index}">
                    <div class="d-flex justify-content-between align-items-center w-100">
                        <span>${email.from || 'Unknown sender'}</span>
                        <small class="text-muted">${emailDate}</small>
                    </div>
                </button>
            </h2>
            <div id="email${index}" class="accordion-collapse collapse ${index === 0 ? 'show' : ''}" data-bs-parent="#emailConversation">
                <div class="accordion-body ${emailClass}">
                    ${emailContent}
                </div>
            </div>
        `;
        conversationContainer.appendChild(emailItem);
    });
}

// Show Error Message
function showError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.remove('d-none');
} 