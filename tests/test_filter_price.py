import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from browser_set_up import browser_set_up

@allure.title("Обработка ввода отрицательных значений")
@allure.feature("Фильтр по цене")
def test_filter_minus_price(browser_set_up):
     # set_filter_price - ввод в фильтр "Диапазон цен (₽)" значения min_price и max_price
    def set_filter_price(driver, min_price, max_price):
        filter_price = driver.find_elements(By.CLASS_NAME, "_filters__input_1iunh_20")
        filter_price[1].send_keys(min_price)
        filter_price[2].send_keys(max_price)
        time.sleep(1)
        WebDriverWait(driver, 10).until(
         EC.invisibility_of_element_located((By.CLASS_NAME, "_fetchingIndicator_imlvm_134"))
         )

        assert (int(filter_price[1].get_attribute("value")) >= 0 or int(filter_price[2].get_attribute("value")) >= 0), f"Поле 'Диапазон цен (₽)' приняло ввод отрицательного значения {min_price} и {max_price}"
        
    driver = browser_set_up
    driver.get("https://cerulean-praline-8e5aa6.netlify.app/") 
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_card__price_15fhn_241"))
    )
    min_price = random.randint(-5000, -1000)
    max_price = random.randint(-500, -1)

    set_filter_price(driver, min_price, max_price)


@allure.title("Проверка роботы фильтра 'Диапазон цен (₽)'")
@allure.feature("Фильтр по цене")
@pytest.mark.repeat(5)
def test_filter_price(browser_set_up):

    # set_filter_price - ввод в фильтр "Диапазон цен (₽)" значения min_price и max_price
    def set_filter_price(driver, min_price, max_price):
        filter_price = driver.find_elements(By.CLASS_NAME, "_filters__input_1iunh_20")
        filter_price[1].send_keys(min_price)
        filter_price[2].send_keys(max_price)
        time.sleep(1)
        WebDriverWait(driver, 10).until(
         EC.invisibility_of_element_located((By.CLASS_NAME, "_fetchingIndicator_imlvm_134"))
         )

    # get_all_price - находит цены всех оъявлений на странице и возвращает их массиом all_price
    def get_all_price(driver):
        price_elements = driver.find_elements(By.CLASS_NAME, "_card__price_15fhn_241")
        all_price_str = [pr.text for pr in price_elements]
        return clear_price(all_price_str)
    
    # clear_price - очищает собранные цены объявлений от лишних символов
    def clear_price(all_price_str):
        all_price = []
        for p in all_price_str:
            clean_price = p.strip().replace('₽', '').replace('&nbsp;', '').replace(' ', '')
            all_price.append(int(clean_price))
        return all_price

    driver = browser_set_up
    driver.get("https://cerulean-praline-8e5aa6.netlify.app/") 
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_card__price_15fhn_241"))
    )
    min_price = random.randint(7000, 10000)
    max_price = random.randint(20000, 70000)
    
    set_filter_price(driver, min_price, max_price)
    all_price = get_all_price(driver)
    assert all((min_price <=  price <= max_price for price in all_price)), f"Неверная работа фильтра диапазона цен. Цены: {all_price} не соответствуют фильтру [{min_price}; {max_price}]"