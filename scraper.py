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

    # 리뷰 내용이 들어 있는 <span class="twc-bg-white"> 태그 선택
    review_spans = soup.select("div.sdp-review__article__list__review__content span.twc-bg-white")

    reviews = [tag.get_text(strip=True) for tag in review_spans if tag.get_text(strip=True)]
    
    return reviews
