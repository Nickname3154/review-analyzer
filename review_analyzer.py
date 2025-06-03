from transformers import AutoTokenizer, AutoModelForSequenceClassification, PreTrainedTokenizerFast, BartForConditionalGeneration
from transformers import pipeline
from collections import Counter

# 1. 감성 분석용 KcBERT 모델 로드
def load_kcbert_sentiment_pipeline():
    model_name = "beomi/KcBERT-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained("beomi/KcBERT-sentiment")  # 감성분석용 fine-tuned 모델
    return pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# 2. 요약용 KoBART 모델 로드
def load_kobart_summarizer():
    model_name = "digit82/kobart-summarization"
    tokenizer = PreTrainedTokenizerFast.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name)
    return tokenizer, model

tokenizer, summarizer_model = load_kobart_summarizer()
sentiment_pipeline = load_kcbert_sentiment()

# 3. 리뷰 요약 함수
def summarize_reviews_kobart(reviews, tokenizer, summarizer_model):
    filtered = [r.strip() for r in reviews if r.strip()]
    if not filtered:
        return "요약할 리뷰가 없습니다."

    text = " ".join(filtered[:20])
    inputs = tokenizer.encode(text, return_tensors="pt", max_length=1024, truncation=True)
    try:
        summary_ids = model.generate(inputs, max_length=128, min_length=30, length_penalty=2.0, num_beams=4)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary
    except Exception as e:
        return f"[요약 실패] 에러: {e}"

# 4. 감정 분석 함수
def analyze_sentiment_kcbert(reviews, sentiment_pipeline):
    filtered = [r.strip() for r in reviews if r.strip()]
    if not filtered:
        return {"긍정": 0, "부정": 0, "에러": "분석할 리뷰가 없습니다."}

    try:
        results = sentiment_pipeline(filtered[:20])
        counter = Counter([res['label'] for res in results])
        return dict(counter)
    except Exception as e:
        return {"에러": str(e)}
