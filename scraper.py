import requests
from bs4 import BeautifulSoup

def get_reviews(product_url):
    # 실제로는 더 많은 페이지 및 예외 처리 필요
    reviews = []
    headers = {"User-Agent": "Mozilla/5.0"}
    for page in range(1, 3):
        review_url = f"{product_url.replace('products', 'product-reviews')}?page={page}"
        response = requests.get(review_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        for tag in soup.select(".sdp-review__article__list__review__content"):
            reviews.append(tag.get_text(strip=True))
    return reviews
