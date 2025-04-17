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
    const sentimentScoreElement = document.getElementById('sentimentScore');
    
    // Set the width of the progress bar (from -1 to 1)
    sentimentMeter.style.width = `${(sentimentScore + 1) * 50}%`;
    sentimentMeter.setAttribute('aria-valuenow', sentimentScore);
    
    // Update the displayed score
    sentimentScoreElement.textContent = sentimentScore.toFixed(2);
    
    // Set the color based on sentiment score
    if (sentimentScore <= -0.5) {
        // Strong negative - red
        sentimentMeter.style.backgroundColor = '#dc3545'; // Bootstrap danger red
    } else if (sentimentScore >= 0.5) {
        // Strong positive - green
        sentimentMeter.style.backgroundColor = '#198754'; // Bootstrap success green
    } else {
        // Neutral or mixed - calculate a color between red and green
        // Map -0.5 to 0 to 0.5 to a value between 0 and 1
        const normalizedScore = (sentimentScore + 0.5) / 1;
        
        // For values between -0.5 and 0, transition from red to yellow
        // For values between 0 and 0.5, transition from yellow to green
        if (normalizedScore <= 0.5) {
            // Red to Yellow (0 to 0.5)
            const redToYellow = normalizedScore * 2; // 0 to 1
            const red = Math.round(220 - (redToYellow * 220)); // 220 is the red component of #dc3545
            const green = Math.round(25 + (redToYellow * 230)); // 25 is the green component of #dc3545, 230 is the difference to yellow
            sentimentMeter.style.backgroundColor = `rgb(${red}, ${green}, 0)`; // Yellow has no blue component
        } else {
            // Yellow to Green (0.5 to 1)
            const yellowToGreen = (normalizedScore - 0.5) * 2; // 0 to 1
            const red = Math.round(220 - (yellowToGreen * 220)); // 220 is the red component of yellow
            const green = Math.round(255 - (yellowToGreen * 97)); // 255 is the green component of yellow, 97 is the difference to #198754
            sentimentMeter.style.backgroundColor = `rgb(${red}, ${green}, 84)`; // 84 is the blue component of #198754
        }
    }
    
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
    
    // No need to filter since we're only receiving merchant emails from the backend
    emails.forEach((email, index) => {
        const emailItem = document.createElement('div');
        emailItem.className = 'accordion-item';
        
        // Format the date
        const emailDate = new Date(email.date).toLocaleString();
        
        // Determine the email class based on sentiment
        let emailClass = '';
        if (email.sentiment_score !== undefined) {
            if (email.sentiment_score > 0.5) {
                emailClass = 'positive-sentiment';
            } else if (email.sentiment_score < -0.5) {
                emailClass = 'negative-sentiment';
            } else {
                emailClass = 'neutral-sentiment';
            }
        }
        
        // Create email header with sender and date
        const emailHeader = `
            <div class="d-flex justify-content-between align-items-center">
                <span>${email.from || 'Unknown sender'}</span>
                <small class="text-muted">${emailDate}</small>
            </div>
        `;
        
        // Create sentiment information if available
        let sentimentInfo = '';
        if (email.sentiment_score !== undefined) {
            sentimentInfo = `
                <div class="sentiment-info mt-2">
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
                    <div class="d-flex justify-content-start">
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