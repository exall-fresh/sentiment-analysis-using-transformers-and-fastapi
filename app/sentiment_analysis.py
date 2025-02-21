from transformers import pipeline

# Load pre-trained sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

def sentiment_analysis(text):
    result = sentiment_pipeline(text)
    return result
