from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time

def get_reviews(url, max_reviews=20):
    # Chrome 옵션 설정 (headless 모드 등)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.binary_location = "/usr/bin/chromium-browser"

    # WebDriver 설정
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    try:
        driver.get(url)
        time.sleep(3)

        # 리뷰 탭 클릭
        try:
            review_tab = driver.find_element(By.XPATH, '//*[@id="btfTab"]/ul[1]/li[2]')
            review_tab.click()
            time.sleep(3)
        except Exception as e:
            print("리뷰 탭 클릭 실패:", e)
            return [f"리뷰 탭 클릭 실패: {e}"]

        # 페이지 소스를 BeautifulSoup으로 파싱
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        articles = soup.find_all('article', class_='sdp-review__article__list', limit=max_reviews)

        reviews = []
        for article in articles:
            content_tag = article.find('div', class_='sdp-review__article__list__review__content')
            if content_tag:
                review_text = content_tag.get_text(strip=True)
                reviews.append(review_text)

        return reviews if reviews else ["리뷰를 찾을 수 없습니다."]

    finally:
        driver.quit()
