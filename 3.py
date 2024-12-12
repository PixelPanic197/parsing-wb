from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Путь к ChromeDriver
chrome_driver_path = "chromedriver.exe"  # Убедитесь, что путь к драйверу правильный

# Настройки браузера
options = Options()
# options.add_argument("--headless")  # Уберите комментарий, если не нужен видимый браузер
options.add_argument("--disable-blink-features=AutomationControlled")

# Инициализация драйвера
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

# Список для хранения ID товаров
product_ids = []

try:
    # Перебор страниц с товарами
    for page in range(1, 18):  # Страницы с 1 по 17
        url = f"https://www.wildberries.ru/seller/10954?sort=popular&page={page}"
        driver.get(url)
        
        # Прокручиваем страницу до конца, чтобы все товары подгрузились
        last_height = driver.execute_script("return document.body.scrollHeight")
        time.sleep(5)
        while True:
            # Прокрутка страницы вниз
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  # Подождите, чтобы страница успела подгрузиться
            
            # Получаем новый размер страницы
            new_height = driver.execute_script("return document.body.scrollHeight")
            
            # Если высота страницы не изменилась, значит, мы дошли до конца
            if new_height == last_height:
                break
            
            last_height = new_height

        # Подождать, чтобы страница окончательно прогрузилась
        time.sleep(10)
        
        # Извлечение ссылок на товары
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".product-card__link")
        
        # Перебор всех ссылок на товары и извлечение ID
        for card in product_cards:
            product_url = card.get_attribute("href")
            # Извлечение ID товара из ссылки
            product_id = product_url.split('/')[4]  # ID товара находится на 4-й позиции в URL
            product_ids.append(product_id)

        print(f"Страница {page} загружена.")

    # Вывод всех ID товаров
    print("Все ID товаров:", product_ids)

finally:
    driver.quit()
