from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

def get_reviews(product_url, max_reviews=20):
    options = Options()
    options.add_argument("--headless")  # Streamlit 환경에서 브라우저 안 띄우도록 설정
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(3)

    try:
        driver.get(product_url)
        time.sleep(2)

        # 리뷰 탭 클릭
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
        print("에러 발생:", e)
        return []

    finally:
        driver.quit()
