import requests
from bs4 import BeautifulSoup

def get_reviews(product_url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(product_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    reviews = []
    for tag in soup.select("div.sdp-review__article__list__review__content span.twc-bg-white"):
        reviews.append(tag.get_text(strip=True))

    return reviews
