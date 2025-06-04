import streamlit as st
from review_analyzer import summarize_reviews_openai, analyze_sentiment_openai

st.title("리뷰 요약 및 감성 분석기 (OpenAI 기반)")

# 사용자에게 OpenAI API 키 입력 받기
api_key = st.text_input("OpenAI API 키를 입력하세요", type="password")

product_url = st.text_input("상품 URL을 입력하세요 :")

if st.button("리뷰 분석 시작"):
    if not api_key:
        st.error("API 키를 입력해야 합니다.")
    else:
        # 샘플 리뷰 리스트
        reviews = [
            "저는 하체 근육이 심해서 이만기 장딴지예요.. 여성 의류는 와이드바지를 사도 종아리쪽 사이즈가 작아서 종아리근육이 더 도드라지더라구요ㅜㅜ "
            "몇 번의 실패 후 걍 남자팬츠로 찾아보는데 스판도 좋고 시원하다고 해서 하나 질러봤습니다. 진짜 바지가 차갑습니다!! 바로 착용해보니 스판 장난아니고 "
            "아빠다리 하고 앉아봤는데 미춌어요. 한 시간 앉을 수 있을 각. 진짜 편합니다."
        ]

        st.success(f"{len(reviews)}개의 리뷰를 불러왔습니다.")

        with st.spinner("요약 및 감정 분석 중..."):
            summary = summarize_reviews_openai(reviews, api_key)
            sentiment = analyze_sentiment_openai(reviews, api_key)

        st.subheader("리뷰 요약")
        st.write(summary)

        st.subheader("분석 결과")
        st.write(sentiment)
