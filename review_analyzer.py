from transformers import pipeline

# Hugging Face 파이프라인 로드
summarizer = pipeline("summarization", model="knkarthick/MEETING_SUMMARY")
sentiment_model = pipeline("sentiment-analysis")

# 리뷰 요약 함수
def summarize_reviews(reviews):
    filtered = [r.strip() for r in reviews if r.strip()]
    if not filtered:
        return "요약할 리뷰가 없습니다."

    joined_text = " ".join(filtered[:20])
    try:
        summary = summarizer(joined_text, max_length=130, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"[요약 실패] 에러: {e}"

# 감정 분석 함수
def analyze_sentiment(reviews):
    filtered = [r.strip() for r in reviews if r.strip()]
    if not filtered:
        return {"POSITIVE": 0, "NEGATIVE": 0, "에러": "분석할 리뷰가 없습니다."}

    try:
        sentiments = sentiment_model(filtered[:20])
        result = {"POSITIVE": 0, "NEGATIVE": 0}
        for s in sentiments:
            label = s['label'].upper()
            if label in result:
                result[label] += 1
            else:
                result[label] = 1
        return result
    except Exception as e:
        return {"에러": str(e)}
