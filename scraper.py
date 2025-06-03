import requests
from bs4 import BeautifulSoup

def get_reviews(product_url):
    reviews = []
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(product_url, headers=headers)
    if response.status_code != 200:
        print(f"[오류] 페이지 요청 실패. 상태 코드: {response.status_code}")
        return reviews

    soup = BeautifulSoup(response.text, "html.parser")
    review_spans = soup.select("span.twc-bg-white")

    for span in review_spans:
        text = span.get_text(separator=" ", strip=True)
        if text:
            reviews.append(text)

    return reviews
