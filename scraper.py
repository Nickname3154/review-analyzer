from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time


def get_reviews(product_url, max_reviews=20):
    """
    쿠팡 상품 URL에서 리뷰 텍스트를 크롤링하여 리스트로 반환합니다.

    Args:
        product_url (str): 쿠팡 상품 상세페이지 URL
        max_reviews (int): 최대 수집할 리뷰 개수 (기본값 20개)

    Returns:
        list[str]: 리뷰 텍스트 리스트
    """
    # 브라우저 옵션 설정
    options = Options()
    options.binary_location = "/usr/bin/chromium"
    options.add_argument("--headless")  # GUI 없이 실행
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # 크롬 드라이버 자동 설치 및 서비스 설정
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(3)

    try:
        # 상품 페이지 로드
        driver.get(product_url)
        time.sleep(2)

        # 리뷰 탭 클릭 (있는 경우)
        try:
            review_tab = driver.find_element(By.XPATH, '//*[@id="btfTab"]/ul[1]/li[2]')
            review_tab.click()
            time.sleep(2)
        except Exception as e:
            print("리뷰 탭 클릭 실패:", e)

        # 페이지에서 리뷰 추출
        soup = BeautifulSoup(driver.page_source, "html.parser")
        articles = soup.find_all("article", class_="sdp-review__article__list js_reviewArticleReviewList")

        reviews = []
        for a in articles:
            content_tag = a.find("div", class_="sdp-review__article__list__review__content js_reviewArticleContent")
            if content_tag:
                review_text = content_tag.get_text(strip=True)
                if review_text:
                    reviews.append(review_text)
            if len(reviews) >= max_reviews:
                break

        return reviews

    except Exception as e:
        print("리뷰 크롤링 중 에러 발생:", e)
        return []

    finally:
        driver.quit()