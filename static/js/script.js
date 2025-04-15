document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('caseForm');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const errorMessage = document.getElementById('errorMessage');
    const resultsSection = document.getElementById('resultsSection');
    const sentimentChart = document.getElementById('sentimentChart');
    let chart = null;

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const caseNumber = document.getElementById('caseNumber').value.trim();
        if (!caseNumber) {
            showError('Please enter a case number');
            return;
        }

        // Show loading spinner and hide other sections
        loadingSpinner.classList.remove('d-none');
        errorMessage.classList.add('d-none');
        resultsSection.classList.add('d-none');

        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ case_number: caseNumber })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'An error occurred while analyzing the case');
            }

            // Update the UI with the results
            updateResults(data);
            
            // Hide loading spinner and show results
            loadingSpinner.classList.add('d-none');
            resultsSection.classList.remove('d-none');
            
            // Add fade-in animation to results
            document.querySelectorAll('.card').forEach(card => {
                card.classList.add('fade-in');
            });

        } catch (error) {
            showError(error.message);
            loadingSpinner.classList.add('d-none');
        }
    });

    function showError(message) {
        errorMessage.textContent = message;
        errorMessage.classList.remove('d-none');
        loadingSpinner.classList.add('d-none');
        resultsSection.classList.add('d-none');
    }

    function updateResults(data) {
        // Update summary statistics
        document.getElementById('totalEmails').textContent = data.total_emails;
        document.getElementById('supportEmails').textContent = data.support_emails;
        document.getElementById('merchantEmails').textContent = data.merchant_emails;
        
        // Update sentiment score
        const sentimentScore = document.getElementById('sentimentScore');
        sentimentScore.textContent = data.sentiment_score.toFixed(2);
        sentimentScore.className = getSentimentClass(data.sentiment_score);
        
        // Update progress bar
        const progressBar = document.getElementById('sentimentProgress');
        progressBar.style.width = `${(data.sentiment_score + 1) * 50}%`;
        progressBar.className = `progress-bar ${getSentimentClass(data.sentiment_score)}`;
        
        // Update sentiment trend chart
        updateSentimentChart(data.sentiment_timeline);
        
        // Update email details
        updateEmailDetails(data.emails);
    }

    function getSentimentClass(score) {
        if (score > 0.3) return 'sentiment-positive';
        if (score < -0.3) return 'sentiment-negative';
        return 'sentiment-neutral';
    }

    function updateSentimentChart(timeline) {
        const ctx = sentimentChart.getContext('2d');
        
        // Destroy existing chart if it exists
        if (chart) {
            chart.destroy();
        }
        
        // Create new chart
        chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: timeline.map(item => new Date(item.date).toLocaleDateString()),
                datasets: [{
                    label: 'Sentiment Score',
                    data: timeline.map(item => item.score),
                    borderColor: '#3498db',
                    backgroundColor: 'rgba(52, 152, 219, 0.1)',
                    tension: 0.4,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        display: false
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `Score: ${context.parsed.y.toFixed(2)}`;
                            }
                        }
                    }
                },
                scales: {
                    y: {
                        min: -1,
                        max: 1,
                        ticks: {
                            stepSize: 0.5
                        }
                    }
                }
            }
        });
    }

    function updateEmailDetails(emails) {
        const emailAccordion = document.getElementById('emailAccordion');
        emailAccordion.innerHTML = '';
        
        emails.forEach((email, index) => {
            const emailHtml = `
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <button class="accordion-button ${index === 0 ? '' : 'collapsed'}" type="button" 
                                data-bs-toggle="collapse" data-bs-target="#email${index}">
                            <div class="d-flex justify-content-between align-items-center w-100">
                                <span>${email.subject}</span>
                                <small class="text-muted ms-2">${new Date(email.date).toLocaleString()}</small>
                            </div>
                        </button>
                    </h2>
                    <div id="email${index}" class="accordion-collapse collapse ${index === 0 ? 'show' : ''}" 
                         data-bs-parent="#emailAccordion">
                        <div class="accordion-body">
                            <div class="mb-3">
                                <strong>From:</strong> ${email.sender}<br>
                                <strong>To:</strong> ${email.recipient}<br>
                                <strong>Date:</strong> ${new Date(email.date).toLocaleString()}
                            </div>
                            <div class="email-content">${email.content}</div>
                            ${email.noteworthy_snippet ? `
                                <div class="noteworthy-snippet">
                                    <strong>Noteworthy:</strong><br>
                                    ${email.noteworthy_snippet}
                                </div>
                            ` : ''}
                        </div>
                    </div>
                </div>
            `;
            emailAccordion.innerHTML += emailHtml;
        });
    }
}); 