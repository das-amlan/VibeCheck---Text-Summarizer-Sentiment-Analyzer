import streamlit as st
from nlp_pipeline.summarizer import summarizer_text
from nlp_pipeline.sentiment_analyzer import sentiment_analyzer

# def main():
#     text = input("Enter a text: ")

#     summary = summarizer_text(text)
#     print("\nSummarized Text: ")
#     print(summary)

#     sentiment = sentiment_analyzer(summary)
#     print("\nSentiment Analysis of Summary: ")
#     print(f"Sentiment: {sentiment['label']}, Confidence Score: {sentiment['score']:.2f}")

# if __name__ == "__main__":
#     main()

st.title("VibeCheck")
st.caption("Text Summarization and Sentiment Analysis")

input_text = st.text_area("Enter your text:", height=200)

if st.button("Analyze"):
    if input_text:
        summary = summarizer_text(input_text)
        st.subheader("Summarized Text:")
        st.write(summary)

        #sentiment
        sentiment = sentiment_analyzer(summary)
        st.subheader("Sentiment Analysis:")
        st.write(f"Sentiment: {sentiment['label']}")
        st.write(f"Confidence Score: {sentiment['score']:.2f}")
    else:
        st.warning("Looks Empty! Please enter some text for analysis.")