import streamlit as st
from scraper import get_reviews
from review_analyzer import summarize_reviews, analyze_sentiment

st.title("쿠팡 리뷰 요약 및 분석기")

product_url = st.text_input("쿠팡 상품 URL을 입력하세요:")

if st.button("리뷰 가져오기 및 분석"):
    with st.spinner("리뷰를 가져오는 중입니다..."):
        reviews = [ "입으려고 구입했는데 넘 괜찮아서 다른색상으로 재구매하게 되었어요.", "허리밴딩이 편하고 차리하게 떨어져서 핏이 괜찮네요.", "가볍게 기본티 입어주면 내추럴하니 넘 맘에 들어요.", "활동하기도 편하고 시원한소재에 구김이 없어서 입고 활동하는데 불편함 없어요.", "작년에 아들 사줬는데 맘에 들어해서 계속 이 바지만 입고 다니더라구요.", "다른색상도 있으면 좋을것 같아 구입해주었는데 넘 좋아하더라구요.", "색상도 예쁘고 모던해서 아무 티셔츠에도 잘 어울려서 만족하고 잘 입을 수 있을것 같아요." , "밝은색상도 구매해야 겠어요." ]

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
