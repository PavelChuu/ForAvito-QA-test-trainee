import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import allure
from browser_set_up import browser_set_up

def add_filter_category(driver):
    filter_category = driver.find_elements(By.CLASS_NAME, "_filters__group_1iunh_1")[4].find_elements(By.XPATH, ".//select[@class='_filters__select_1iunh_21']")[0]
    return filter_category

# get_all_category - находит категории всех объявлениях на странице 
def get_all_category(driver):
    category_elements = []
    all_category_str = []
    category_elements = driver.find_elements(By.CLASS_NAME, "_card__category_15fhn_259")
    all_category_str = [cat.text for cat in category_elements]
    return(all_category_str)

@allure.title("Проверка выбора категории 'Электроника'")
@allure.feature("Фильтр категории")
def test_category_electronics(browser_set_up):
    driver = browser_set_up
    driver.get("https://cerulean-praline-8e5aa6.netlify.app/") 
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_card__price_15fhn_241"))
    )
    filter_category = add_filter_category(driver)
    filter_category.click()
    filter_category.find_elements(By.XPATH, ".//option[@value='0']")[0].click()
    select_category = filter_category.find_elements(By.XPATH, ".//option[@value='0']")[0].text
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "_fetchingIndicator_imlvm_134"))
    )
    filter_category.click()
    assert all(select_category == category for category in get_all_category(driver)), f"Не работает фильтр по категории 'Электроника'"

@allure.title("Проверка выбора категории 'Недвижимость'")
@allure.feature("Фильтр категории")
def test_categoty_estate(browser_set_up):
    driver = browser_set_up
    driver.get("https://cerulean-praline-8e5aa6.netlify.app/") 
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_card__price_15fhn_241"))
    )
    filter_category = add_filter_category(driver)
    filter_category.click()
    filter_category.find_elements(By.XPATH, ".//option[@value='1']")[0].click()
    select_category = filter_category.find_elements(By.XPATH, ".//option[@value='1']")[0].text
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "_fetchingIndicator_imlvm_134"))
    )
    filter_category.click()
    assert all(select_category == category for category in get_all_category(driver)), f"Не работает фильтр по категории 'Недвижимость'"
 
@allure.title("Проверка выбора категории 'Транспорт'")
@allure.feature("Фильтр категории")
def test_categoty_transport(browser_set_up):
    driver = browser_set_up
    driver.get("https://cerulean-praline-8e5aa6.netlify.app/") 
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_card__price_15fhn_241"))
    )
    filter_category = add_filter_category(driver)
    filter_category.click()
    filter_category.find_elements(By.XPATH, ".//option[@value='2']")[0].click()
    select_category = filter_category.find_elements(By.XPATH, ".//option[@value='2']")[0].text
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "_fetchingIndicator_imlvm_134"))
    )
    filter_category.click()
    assert all(select_category == category for category in get_all_category(driver)), f"Не работает фильтр по категории 'Транспорт'"      

@allure.title("Проверка выбора категории 'Работа'")
@allure.feature("Фильтр категории")
def test_categoty_work(browser_set_up):
    driver = browser_set_up
    driver.get("https://cerulean-praline-8e5aa6.netlify.app/") 
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_card__price_15fhn_241"))
    )
    filter_category = add_filter_category(driver)
    filter_category.click()
    filter_category.find_elements(By.XPATH, ".//option[@value='3']")[0].click()
    select_category = filter_category.find_elements(By.XPATH, ".//option[@value='3']")[0].text
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "_fetchingIndicator_imlvm_134"))
    )
    filter_category.click()
    assert all(select_category == category for category in get_all_category(driver)), f"Не работает фильтр по категории 'Работа'"  

@allure.title("Проверка выбора категории 'Услуги'")
@allure.feature("Фильтр категории")   
def test_categoty_services(browser_set_up):
    driver = browser_set_up
    driver.get("https://cerulean-praline-8e5aa6.netlify.app/") 
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_card__price_15fhn_241"))
    )
    filter_category = add_filter_category(driver)
    filter_category.click()
    filter_category.find_elements(By.XPATH, ".//option[@value='4']")[0].click()
    select_category = filter_category.find_elements(By.XPATH, ".//option[@value='4']")[0].text
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "_fetchingIndicator_imlvm_134"))
    )
    filter_category.click()
    assert all(select_category == category for category in get_all_category(driver)), f"Не работает фильтр по категории 'Услуги'"        
 
@allure.title("Проверка выбора категории 'Животные'")
@allure.feature("Фильтр категории")  
def test_categoty_animal(browser_set_up):
    driver = browser_set_up
    driver.get("https://cerulean-praline-8e5aa6.netlify.app/") 
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_card__price_15fhn_241"))
    )
    filter_category = add_filter_category(driver)
    filter_category.click()
    filter_category.find_elements(By.XPATH, ".//option[@value='5']")[0].click()
    select_category = filter_category.find_elements(By.XPATH, ".//option[@value='5']")[0].text
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "_fetchingIndicator_imlvm_134"))
    )
    filter_category.click()
    assert all(select_category == category for category in get_all_category(driver)), f"Не работает фильтр по категории 'Животные'"      

@allure.title("Проверка выбора категории 'Мода'")
@allure.feature("Фильтр категории")     
def test_categoty_mode(browser_set_up):
    driver = browser_set_up
    driver.get("https://cerulean-praline-8e5aa6.netlify.app/") 
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_card__price_15fhn_241"))
    )
    filter_category = add_filter_category(driver)
    filter_category.click()
    filter_category.find_elements(By.XPATH, ".//option[@value='6']")[0].click()
    select_category = filter_category.find_elements(By.XPATH, ".//option[@value='6']")[0].text
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "_fetchingIndicator_imlvm_134"))
    )
    filter_category.click()
    assert all(select_category == category for category in get_all_category(driver)), f"Не работает фильтр по категории 'Мода'"
  
@allure.title("Проверка выбора категории 'Детское'")
@allure.feature("Фильтр категории")     
def test_categoty_child(browser_set_up):
    driver = browser_set_up
    driver.get("https://cerulean-praline-8e5aa6.netlify.app/") 
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "_card__price_15fhn_241"))
    )
    filter_category = add_filter_category(driver)
    filter_category.click()
    filter_category.find_elements(By.XPATH, ".//option[@value='7']")[0].click()
    select_category = filter_category.find_elements(By.XPATH, ".//option[@value='7']")[0].text
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "_fetchingIndicator_imlvm_134"))
    )
    filter_category.click()
    assert all(select_category == category for category in get_all_category(driver)), f"Не работает фильтр по категории 'Детское'"
