import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser_set_up import browser_set_up

@allure.title("Проверка работы кнопки 'Обновить'")
@allure.feature("Проверка роботы таймера обновления статистики ")
@pytest.mark.timer
def test_update_timer(browser_set_up):
    driver = browser_set_up
    driver.get("https://cerulean-praline-8e5aa6.netlify.app") 
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_card__price_15fhn_241"))
    )
    driver.find_elements(By.CLASS_NAME, "_icon_14hw7_85")[1].click()
    WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "_timeValue_ir5wu_112"), "4:57")
    )
    driver.find_elements(By.CLASS_NAME, "_refreshButton_ir5wu_16")[0].click()
    timer_text = driver.find_elements(By.CLASS_NAME, "_timeValue_ir5wu_112")[0].text
    assert (timer_text == "5:00"), "Ошибка: кнопка 'Обновить' не обновляет таймер"

@allure.title("Проверка работы кнопки Остановки/Старта таймера")
@allure.feature("Проверка роботы таймера обновления статистики ")
@pytest.mark.timer
#   test_stop_start_timer - проверка работы кнопки Остановки/Старта таймера
def test_stop_start_timer(browser_set_up):
    driver = browser_set_up
    driver.get("https://cerulean-praline-8e5aa6.netlify.app") 
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_card__price_15fhn_241"))
    )
    driver.find_elements(By.CLASS_NAME, "_icon_14hw7_85")[1].click()
    WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "_timeValue_ir5wu_112"), "4:59")
    )
    driver.find_elements(By.CLASS_NAME, "_toggleIcon_ir5wu_94")[0].click()
    stop = driver.find_elements(By.CLASS_NAME, "_disabled_ir5wu_136")[0].text
    assert (stop == "Автообновление выключено"), "Кнопка кнопка остановки таймера не срабатывает"
    driver.find_elements(By.CLASS_NAME, "_toggleIcon_ir5wu_94")[0].click()
    try:
        timer_text = driver.find_elements(By.CLASS_NAME, "_timeValue_ir5wu_112")[0].text
    except: timer_text = 0
    assert (timer_text == "5:00"), "Ошибка: Кнопка запуска таймера не срабатывает"