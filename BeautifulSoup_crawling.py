import requests
from bs4 import BeautifulSoup
import time
import re

def get_gmarket_reviews(goodscode, max_pages=3, max_reviews=20):
    """
    G마켓 상품 코드 (goodscode)를 기반으로 리뷰 텍스트를 크롤링하는 함수
    - goodscode: G마켓 상품 페이지의 goodscode 파라미터
    - max_pages: 최대 페이지 수
    - max_reviews: 최대 리뷰 개수
    
    HTML이 정적으로 렌더링된 리뷰를 수집
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0 Safari/537.36"
        )
    }
    reviews = []

    for page in range(1, max_pages + 1):
        url = f"https://item.gmarket.co.kr/Item?goodscode={goodscode}&page={page}"
        res = requests.get(url, headers=headers)
        if res.status_code != 200:
            print(f"[Error] 페이지 로드 실패 {res.status_code} (페이지 {page})")
            break

        soup = BeautifulSoup(res.text, "html.parser")
        review_divs = soup.select("div.review__section__content")

        if not review_divs:
            print("⚠️ 리뷰를 찾지 못했습니다 (정적 HTML 리뷰 없음)")
            break

        for div in review_divs:
            text = re.sub(r"\s+", " ", div.get_text(strip=True))
            reviews.append(text)
            if len(reviews) >= max_reviews:
                break

        if len(reviews) >= max_reviews:
            break

        time.sleep(0.5)

    return reviews

if __name__ == "__main__":
    goodscode = "1806672542"  # 테스트용 상품 코드
    result = get_gmarket_reviews(goodscode, max_pages=5, max_reviews=15)
    print(f"총 {len(result)}개의 리뷰 수집됨:\n")
    for i, r in enumerate(result, 1):
        print(f"{i}. {r}")
