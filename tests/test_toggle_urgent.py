import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from browser_set_up import browser_set_up

@allure.title("Проверка работы тогла 'Только строчные'")
@allure.feature("Проверка роботы таймера обновления статистики ")
@pytest.mark.toggle_urgent
def test_toggle_urgent(browser_set_up):
    
    driver = browser_set_up
    driver.get("https://cerulean-praline-8e5aa6.netlify.app/") 
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_card__price_15fhn_241"))
    )

    driver.find_elements(By.CLASS_NAME, "_filtersBar__controls_1lsyo_43")[0].find_element(By.XPATH, ".//span[@class='_urgentToggle__slider_h1vv9_21']").click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(
         EC.invisibility_of_element_located((By.CLASS_NAME, "_fetchingIndicator_imlvm_134"))
         )

    mark_cards = driver.find_elements(By.CLASS_NAME, "_card__badges_15fhn_128")
    for card in mark_cards:
        assert card.text == "Срочно" , "Ошибка в работе тогла 'Только срочные', найдены объявление без отметки 'Срочно'"