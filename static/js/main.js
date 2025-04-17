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
    
    // Set the color based on sentiment score using a consistent gradient
    sentimentMeter.style.backgroundColor = getSentimentColor(sentimentScore);
    
    // Update sentiment chart
    updateSentimentChart(data.sentiment_timeline);
    
    // Update email conversation
    updateEmailConversation(data.emails);
    
    // Show results section
    resultsSection.classList.remove('d-none');
}

// Helper function to get sentiment color based on score
function getSentimentColor(score) {
    // Create a gradient from dark red (-1) to yellow (0) to dark green (1)
    if (score <= -0.5) {
        // Strong negative - dark red
        return '#8B0000'; // Dark red
    } else if (score >= 0.5) {
        // Strong positive - dark green
        return '#006400'; // Dark green
    } else {
        // For scores between -0.5 and 0.5, create a smooth transition
        if (score < 0) {
            // From dark red to yellow
            const normalizedScore = (score + 0.5) / 0.5; // 0 to 1
            const red = Math.round(139 - (normalizedScore * 139)); // 139 is the red component of dark red
            const green = Math.round(normalizedScore * 255); // 255 is the green component of yellow
            return `rgb(${red}, ${green}, 0)`; // Yellow has no blue component
        } else {
            // From yellow to dark green
            const normalizedScore = score / 0.5; // 0 to 1
            const red = Math.round(255 - (normalizedScore * 255)); // 255 is the red component of yellow
            const green = Math.round(255 - (normalizedScore * 191)); // 255 is the green component of yellow, 191 is the difference to dark green
            return `rgb(${red}, ${green}, 0)`; // Dark green has no blue component
        }
    }
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