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
