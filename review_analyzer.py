import os
import openai
from collections import Counter

# OpenAI API 키 설정 (환경 변수 OPENAI_API_KEY를 사용하는 방식)
openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_reviews_openai(reviews):
    if not reviews:
        return "요약할 리뷰가 없습니다."

    joined_reviews = "\n".join(reviews[:20])

    prompt = f"""다음은 한국어로 된 상품 리뷰입니다. 이 리뷰들을 읽고 핵심 내용을 요약해 주세요:

{joined_reviews}

요약:"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 한국어 리뷰 요약 전문가입니다."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=300,
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"[요약 실패] 에러: {e}"

def analyze_sentiment_openai(reviews):
    if not reviews:
        return {"긍정": 0, "부정": 0, "중립": 0}

    prompt = "다음 리뷰들을 각각 긍정, 부정, 중립으로 분류해 주세요. 각 줄에 하나의 리뷰가 있습니다:\n\n"
    prompt += "\n".join(reviews[:20])
    prompt += "\n\n각 리뷰에 대해 '긍정', '부정', '중립' 중 하나로만 결과를 출력해 주세요. 순서대로 한 줄씩 출력해 주세요."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 감정 분석 전문가입니다."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=300,
        )
        output = response.choices[0].message["content"].strip().splitlines()
        counter = Counter(output)
        return dict(counter)
    except Exception as e:
        return {"에러": str(e)}
