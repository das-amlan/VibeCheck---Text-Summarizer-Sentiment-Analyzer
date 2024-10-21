from transformers import pipeline

sentiment_pipe = pipeline("text-classification", 
                          model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

def sentiment_analyzer(text):
    sentiment = sentiment_pipe(text)
    return sentiment[0]