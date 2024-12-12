from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Путь к ChromeDriver
chrome_driver_path = "chromedriver.exe"  # Убедитесь, что путь к драйверу правильный

# Настройки браузера
options = Options()
#options.add_argument("--headless")  # Убрать комментарий, если нужен фоновый режим
options.add_argument("--disable-blink-features=AutomationControlled")

# Инициализация драйвера
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # URL страницы
    url = "https://www.wildberries.ru/catalog/176080203/detail.aspx"
    driver.get(url)

    # Подождать загрузку страницы
    time.sleep(15)

    # Извлечение текущей цены
    final_price = driver.find_element(By.CSS_SELECTOR, ".price-block__final-price.wallet").text.strip()
    
    # Извлечение старой цены (перечеркнутой)
    old_price = driver.find_element(By.CSS_SELECTOR, ".price-block__old-price span").text.strip()

    # Извлечение оценки и количества отзывов
    reviews_info = driver.find_element(By.CSS_SELECTOR, ".product-page__reviews-info")
    rating = reviews_info.find_element(By.CSS_SELECTOR, ".product-page__reviews-icon.address-rate-mini").text.strip()
    reviews_count = reviews_info.find_element(By.CSS_SELECTOR, ".product-page__reviews-text.j-product-page-reviews-text").text.strip()

    print("Текущая цена:", final_price)
    print("Старая цена:", old_price)
    print("Оценка:", rating)
    print("Количество отзывов:", reviews_count)

finally:
    driver.quit()
