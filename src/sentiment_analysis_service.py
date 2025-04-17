import os
import json
import re
from dotenv import load_dotenv
from portkey_ai import Portkey

# Load environment variables
load_dotenv()

class SentimentAnalysisService:
    """Service for sentiment analysis using Gemini through Portkey."""
    
    def __init__(self):
        """Initialize the sentiment analysis service with Portkey configuration."""
        self.api_key = os.getenv('PORTKEY_API_KEY')
        self.virtual_key = os.getenv('VERTEX_PORTKEY_VIRTUAL_KEY')
        self.base_url = os.getenv('PORTKEY_GATEWAY_URL')
        
        if not all([self.api_key, self.virtual_key, self.base_url]):
            raise ValueError("Missing required Portkey configuration. Please check your .env file.")
        
        # Initialize Portkey client
        self.portkey = Portkey(
            api_key=self.api_key,
            virtual_key=self.virtual_key,
            base_url=self.base_url
        )
    
    def analyze(self, text):
        """
        Analyze the sentiment of the given text using Gemini through Portkey.
        
        Args:
            text (str): The text to analyze.
            
        Returns:
            dict: A dictionary containing sentiment analysis results with the following fields:
                - score: a number between -1 and 1 where -1 is very negative, 0 is neutral, and 1 is very positive
                - category: one of ['Positive', 'Negative', 'Neutral']
                - emotions: list of primary emotions detected
                - explanation: brief explanation of the sentiment analysis
        """
        try:
            # Clean and prepare the text
            text = text.strip()
            if not text:
                return {
                    'score': 0,
                    'category': 'Neutral',
                    'emotions': [],
                    'explanation': 'No text provided for analysis'
                }
            
            # Prepare messages for the agent
            messages = [
                {
                    "role": "system",
                    "content": """You are a sentiment analysis expert. Your task is to analyze the sentiment of the given text and provide a response in JSON format with the following fields:
                    - score: a number between -1 and 1 where -1 is very negative, 0 is neutral, and 1 is very positive
                    - category: one of ['Positive', 'Negative', 'Neutral']
                    - emotions: list of primary emotions detected
                    - explanation: brief explanation of the sentiment analysis
                    """,
                },
                {
                    "role": "user",
                    "content": f"Analyze the sentiment in this text:\n{text}",
                },
            ]
            
            # Invoke the Portkey API
            response = self.portkey.chat.completions.create(
                model="gemini-1.5-flash-002",
                messages=messages,
                temperature=0,
            )
            
            # Extract the response content
            content = response.choices[0].message.content
            
            # Try to parse the JSON from the response
            try:
                # First, try to find JSON in the response (in case there's additional text)
                json_match = re.search(r'\{.*\}', content, re.DOTALL)
                if json_match:
                    json_str = json_match.group(0)
                    sentiment_result = json.loads(json_str)
                else:
                    # If no JSON found, create a default response
                    sentiment_result = {
                        'score': 0,
                        'category': 'Neutral',
                        'emotions': [],
                        'explanation': 'Could not parse sentiment analysis result'
                    }
            except json.JSONDecodeError:
                # If the response is not valid JSON, create a default response
                sentiment_result = {
                    'score': 0,
                    'category': 'Neutral',
                    'emotions': [],
                    'explanation': 'Could not parse sentiment analysis result'
                }
            
            return sentiment_result
            
        except Exception as e:
            print(f"Error in sentiment analysis: {str(e)}")
            return {
                'score': 0,
                'category': 'Neutral',
                'emotions': [],
                'explanation': f'Error analyzing sentiment: {str(e)}'
            }
    
    def extract_noteworthy_snippets(self, text, sentiment_score):
        """
        Extract noteworthy snippets from the email text based on sentiment.
        
        Args:
            text (str): The text to extract snippets from.
            sentiment_score (float): The sentiment score of the text.
            
        Returns:
            list: A list of noteworthy snippets.
        """
        if not text:
            return []
        
        # Clean the text
        clean_text = re.sub(r'<[^>]+>', '', text)
        
        # Split into sentences
        sentences = re.split(r'(?<=[.!?])\s+', clean_text)
        
        # Filter sentences based on sentiment
        if sentiment_score < -0.5:
            # For negative sentiment, look for sentences with negative words
            negative_words = ['angry', 'frustrated', 'unhappy', 'disappointed', 'terrible', 'bad', 'worst', 'horrible', 'upset', 'annoyed']
            return [s for s in sentences if any(word in s.lower() for word in negative_words)]
        elif sentiment_score > 0.5:
            # For positive sentiment, look for sentences with positive words
            positive_words = ['happy', 'pleased', 'thank', 'great', 'excellent', 'good', 'wonderful', 'amazing', 'appreciate', 'satisfied']
            return [s for s in sentences if any(word in s.lower() for word in positive_words)]
        else:
            # For neutral sentiment, return a few sentences from the middle
            return sentences[:3] if len(sentences) > 3 else sentences 