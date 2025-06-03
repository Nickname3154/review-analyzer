from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

def get_reviews(product_url, max_reviews=20):
    options = Options()
    options.add_argument("--headless")  # 브라우저 창 안 띄움
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(product_url)

    time.sleep(2)  # 페이지 로딩 대기

    reviews = set()
    last_height = driver.execute_script("return document.body.scrollHeight")
    scroll_count = 0

    while len(reviews) < max_reviews and scroll_count < 10:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # 스크롤 후 로딩 대기

        # 리뷰 텍스트 요소 추출
        review_elements = driver.find_elements(By.CSS_SELECTOR, "div.sdp-review__article__list__review__content span")

        for elem in review_elements:
            reviews.add(elem.text)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # 더 이상 로드되는 내용이 없을 경우 종료
        last_height = new_height
        scroll_count += 1

    driver.quit()
    return list(reviews)[:max_reviews]
