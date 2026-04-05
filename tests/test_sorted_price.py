import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from browser_set_up import browser_set_up

@allure.title("Проверка роботы сорировки цены")
@allure.feature("Сортировка цены")
@pytest.mark.sorted_price
def test_sorted_price(browser_set_up):
    # get_all_price - находит цены всех товаров на странице и возвращает их массиом all_price
    def get_all_price(driver):
        price_elements = driver.find_elements(By.CLASS_NAME, "_card__price_15fhn_241")
        all_price_str = [pr.text for pr in price_elements]
        all_price = []
        for p in all_price_str:
            clean_price = p.strip().replace('₽', '').replace('&nbsp;', '').replace(' ', '')
            all_price.append(int(clean_price))
        return all_price
    
    @allure.step("Проверка работы сортировки цены по убыванию")
    def sorted_price_desc():
        sorted = driver.find_elements(By.CLASS_NAME, "_filters__group_1iunh_1")
        sorted[1].click()
        sorted[1].find_elements(By.XPATH, ".//select[@class='_filters__select_1iunh_21']")[0].find_elements(By.XPATH, ".//option[@value='price']")[0].click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(
         EC.invisibility_of_element_located((By.CLASS_NAME, "_fetchingIndicator_imlvm_134"))
         )
        all_price = get_all_price(driver)
        assert all(all_price[0] > price for price in all_price[1:]), "Не работает сортировка цены по убыванию"

    @allure.step("Проверка работы сортировки цены по возрастанию")
    def sorted_price_asc():
        sorted = driver.find_elements(By.CLASS_NAME, "_filters__group_1iunh_1")
        sorted[2].click()
        sorted[2].find_elements(By.XPATH, ".//select[@class='_filters__select_1iunh_21']")[0].find_elements(By.XPATH, ".//option[@value='asc']")[0].click()
        time.sleep(1)
        WebDriverWait(driver, 10).until(
         EC.invisibility_of_element_located((By.CLASS_NAME, "_fetchingIndicator_imlvm_134"))
         )
        all_price = get_all_price(driver)
        print(all_price)
        assert all(all_price[0] < price for price in all_price[1:]), "Не работает сортировка цены по возрастанию"

    driver = browser_set_up
    driver.get("https://cerulean-praline-8e5aa6.netlify.app/") 
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_card__price_15fhn_241"))
    )
    sorted_price_desc()
    sorted_price_asc()