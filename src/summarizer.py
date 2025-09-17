from transformers import pipeline

def get_summary(emails, max_len=60):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    joined_text = " ".join(emails)
    summary = summarizer(joined_text, max_length=max_len, min_length=15, do_sample=False)
    return summary[0]['summary_text']
