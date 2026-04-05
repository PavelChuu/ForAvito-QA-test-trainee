from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

    # browser_set_up - передаём настройки driver. Есть возможность имитировать троттлинг сети 
@pytest.fixture()
def browser_set_up():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.execute_cdp_cmd('Network.emulateNetworkConditions', {
    'offline': False,               # Имитация отключённого интернета, принимает значение True или False (по умолчанию: False)
    'latency': 0,                   # Задержка сети в ms (по умолчанию: 0 ms)
    'downloadThroughput': -1,       # Скорость загрузки в Мбит/с (по умолчанию: -1)
    'uploadThroughput': -1          # Скорость выгрузки в Мбит/с (по умолчанию: -1)
})
    yield driver
    driver.quit()

# mobile_browser_set_up - - передаём настройки мобильного driver. Есть возможность имитировать троттлинг сети, размеры экрана и модель телефона
@pytest.fixture()
def mobile_browser_set_up():
    mobile_emulation = {
    "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },    # Размеры экрана
    "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    }

    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(options=chrome_options)
    driver.execute_cdp_cmd('Network.emulateNetworkConditions', {
    'offline': False,               # Имитация отключённого интернета, принимает значение True или False (по умолчанию: False)
    'latency': 0,                   # Задержка сети в ms (по умолчанию: 0 ms)
    'downloadThroughput': -1,       # Скорость загрузки в Мбит/с (по умолчанию: -1)
    'uploadThroughput': -1          # Скорость выгрузки в Мбит/с (по умолчанию: -1)
    })
    yield driver
    driver.quit()