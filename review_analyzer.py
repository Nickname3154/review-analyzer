from openai import OpenAI

client = OpenAI()  # 환경변수 OPENAI_API_KEY 또는 Streamlit secrets에서 자동 로드됨

def summarize_reviews_openai(reviews):
    try:
        text = "\n".join(reviews[:20])  # 너무 긴 경우 요약 제한
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 리뷰 요약 전문가입니다."},
                {"role": "user", "content": f"다음 리뷰들을 간결하고 핵심적으로 요약해줘:\n{text}"}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[요약 실패] 에러: {str(e)}"

def analyze_sentiment_openai(reviews):
    try:
        text = "\n".join(reviews[:20])
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 감정 분석 전문가입니다."},
                {"role": "user", "content": f"다음 리뷰들을 보고 긍정 또는 부정으로 분석한 뒤 각각 몇 개씩 있는지 요약해줘:\n{text}"}
            ],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"[감정 분석 실패] 에러: {str(e)}"
