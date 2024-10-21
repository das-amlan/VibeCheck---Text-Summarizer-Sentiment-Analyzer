from nlp_pipeline.summarizer import summarizer_text
from nlp_pipeline.sentiment_analyzer import sentiment_analyzer

def main():
    text = input("Enter a text: ")

    summary = summarizer_text(text)
    print("\nSummarized Text: ")
    print(summary)

    sentiment = sentiment_analyzer(summary)
    print("\nSentiment Analysis of Summary: ")
    print(f"Sentiment: {sentiment['label']}, Confidence Score: {sentiment['score']:.2f}")

if __name__ == "__main__":
    main()