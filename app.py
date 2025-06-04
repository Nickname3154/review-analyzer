import streamlit as st
from review_analyzer import summarize_reviews_openai, analyze_sentiment_openai

st.title("리뷰 요약 및 감정 분석 (OpenAI 기반)")

product_url = st.text_input("상품 URL을 입력하세요:")

if st.button("리뷰 가져오기 및 분석"):
    # 테스트용 샘플 리뷰. 실제 크롤링 연동 시 get_reviews(product_url)로 변경 가능
    reviews = [
        "저는 하체 근육이 심해서 이만기 장딴지예요..여성 의류는 와이드바지를 사도 종아리쪽 사이즈가 작아서 종아리근육이 더 도드라지더라구요ㅜㅜ 몇번의 실패후 걍 남자팬츠로 찾아보는데 스판도 좋고 시원하다고 해서 하나 질러봤습니다.",
        "바지가 진짜 시원하고 편해서 하루 종일 입고 있어도 부담이 없어요.",
        "통이 좀 넓긴 하지만 그게 오히려 스타일리시해서 좋아요.",
        "회사에서도 입기 무난하고 재질도 깔끔합니다.",
        "더운 여름에 하나 더 사고 싶을 정도예요."
    ]

    if not reviews:
        st.warning("리뷰를 가져오지 못했습니다. URL이 맞는지, 혹은 리뷰가 있는 상품인지 확인해주세요.")
    else:
        st.success(f"{len(reviews)}개의 리뷰를 가져왔습니다!")

        with st.spinner("OpenAI 기반으로 요약 및 분석 중입니다..."):
            summary = summarize_reviews_openai(reviews)
            sentiment = analyze_sentiment_openai(reviews)

        st.subheader("리뷰 요약")
        st.write(summary)

        st.subheader("감성 분석 결과")
        st.write(sentiment)
