import requests
from bs4 import BeautifulSoup

def get_reviews(product_url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(product_url, headers=headers)
    if response.status_code != 200:
        print(f"요청 실패: {response.status_code}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")

    # 리뷰 전체 article 태그 찾기
    articles = soup.find_all("article", class_="sdp-review__article__list")

    reviews = []

    for article in articles:
        # 리뷰 본문 span 태그 (twc-bg-white 클래스 내부 텍스트 추출)
        review_span = article.select_one("div.sdp-review__article__list__review__content span.twc-bg-white")
        if review_span:
            review_text = review_span.get_text(separator="\n", strip=True)
            reviews.append(review_text)

    return reviews
