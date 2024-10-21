from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small")

def summarizer_text(text):
    # summary = summarizer(text, 
    #                      max_length = 150,
    #                      min_length = 30,
    #                      do_sample = False)
    # Calculate the max_length dynamically based on the input length
    input_length = len(text.split())
    
    # Set a more appropriate max_length, with a minimum value
    max_length = min(150, int(input_length * 1.5))  # 1.5x the input length
    min_length = min(30, input_length)  # Ensure min_length doesn't exceed input length
    
    # Run the text through the summarization pipeline
    summary = summarizer(text, 
                         max_length=max_length, 
                         min_length=min_length, 
                         do_sample=False)
    
    return summary[0]["summary_text"]