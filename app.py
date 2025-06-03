import streamlit as st
from scraper import get_reviews
from review_analyzer import summarize_reviews, analyze_sentiment

st.title("쿠팡 리뷰 요약 및 분석기")

product_url = st.text_input("쿠팡 상품 URL을 입력하세요:")

if st.button("리뷰 가져오기 및 분석"):
    with st.spinner("리뷰를 가져오는 중입니다..."):
        reviews = get_reviews(product_url)

    if not reviews:
        st.warning("리뷰를 가져오지 못했습니다. URL이 맞는지, 혹은 리뷰가 있는 상품인지 확인해주세요.")
    else:
        st.success(f"{len(reviews)}개의 리뷰를 가져왔습니다!")

        with st.spinner("요약 및 분석 중입니다..."):
            summary = summarize_reviews(reviews)
            sentiment = analyze_sentiment(reviews)

        st.subheader("리뷰 요약")
        st.write(summary)

        st.subheader("감성 분석")
        st.write(sentiment)
