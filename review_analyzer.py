from transformers import pipeline

summarizer = pipeline("summarization", model="knkarthick/MEETING_SUMMARY")
sentiment_model = pipeline("sentiment-analysis")

def summarize_reviews(reviews):
    joined_text = " ".join(reviews[:20])  # 긴 텍스트 요약을 위해 일부만 사용
    summary = summarizer(joined_text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']

def analyze_sentiment(reviews):
    sentiments = sentiment_model(reviews[:20])  # 일부만 사용
    result = {"POSITIVE": 0, "NEGATIVE": 0}
    for s in sentiments:
        result[s['label']] += 1
    return result
