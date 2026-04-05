import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser_set_up import mobile_browser_set_up

@allure.title("Проверка работы кнопки смены темы на мобильном устройстве")
@allure.feature("Изменение темы")
@pytest.mark.change_theme
def test_change_theme(mobile_browser_set_up):
    
    driver = mobile_browser_set_up
    driver.get("https://cerulean-praline-8e5aa6.netlify.app") 
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_card__price_15fhn_241"))
    )

    driver.find_elements(By.CLASS_NAME, "_themeToggle_127us_1")[0].click() 
    body = driver.find_element(By.ID, "root")
    initial_color = body.value_of_css_property("background-color") 
    assert (initial_color == "rgba(255, 255, 255, 1)"), "Не работает кнопка измененя темы страницы с тёмной на светлую"
    driver.find_elements(By.CLASS_NAME, "_themeToggle_127us_1")[0].click()
    body = driver.find_element(By.ID, "root")
    initial_color = body.value_of_css_property("background-color")
    assert (initial_color == "rgba(26, 26, 26, 1)"), "Не работает кнопка измененя темы страницы с светлой на тёмную"