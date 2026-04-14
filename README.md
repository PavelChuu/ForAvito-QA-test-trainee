# Тестовое задание дла Avito tech
## Кратко о репозитории
[**Task-1-Find-a-bug.md**](https://github.com/PavelChuu/ForAvito-QA-test-trainee/blob/main/Task-1-Find-a-bug.md) - хранит в себе решение "Задание 1: Скриншот с багами"<br/>
[**TESTCASES.md**](https://github.com/PavelChuu/ForAvito-QA-test-trainee/blob/main/TESTCASES.md) - хранит в себе тест-кейсы  для "Задание 2.2: Тесты UI"<br/>
[**BUGS.md**](https://github.com/PavelChuu/ForAvito-QA-test-trainee/blob/main/BUGS.md) - хранит в себе баг-репорты для "Задание 2.2: Тесты UI"<br/>
[**tests**](https://github.com/PavelChuu/ForAvito-QA-test-trainee/tree/main/tests) - хранит в себе авто-тесты и настройки драйвера для "Задание 2.2: Тесты UI"<br/>
[**requirements.txt**](https://github.com/PavelChuu/ForAvito-QA-test-trainee/blob/main/requirements.txt) - список используемых фреймворков и т.п.

## Как запускать авто-тесты
1. Клонировать репозиторий или скачать zip-архив и разархивировать его в удобное место
2. Открыть проект на любом удобном интерпретаторе Python  (рекомендую: Visual Studio Code)
3. Создать venv окружение<br/>
   3.1 Нажать Ctrl+Shift+P или F1<br/>
   3.2 Ввести **Python: Create Environment**<br/>
   3.3 Выбрать **venv**<br/>
   3.4 Выбрать желаемую версию Python (рекомендую: Python 3.14)<br/>
   3.5 Название папки оставить **.venv**<br/>
   3.6 В конце может предложить загрузить окружение используя [**requirements.txt**](https://github.com/PavelChuu/ForAvito-QA-test-trainee/blob/main/requirements.txt). Выбрать его и создать venv. Если [**requirements.txt**](https://github.com/PavelChuu/ForAvito-QA-test-trainee/blob/main/requirements.txt) не использовалось, то после создания **venv** необходимо в терминал ввести **pip install -r requirements.txt**<br/>
   3.7 Дождаться загрузки окружения<br/>
4. Открыть терминал и ввести в него **pytest --alluredir=./allure-results**
5. Дождаться прогона авто-тестов<br/>

>[!IMPORTANT]
>В проекте подключён Allure Report. Если на ПК установлен Allure CLI можно проверить результаты авто-тестов. В терминал ввести **allure serve allure-results**, в браузере откроется Allure Report с результатами авто-тестов. После проверки результатов, Allure Report нужно закрыть через терминал

> [!WARNING]
>Перед каждым новым запуском авто-тестов рекомендуется очищать папку **allure-results**

## Дополнительные возможности
Имеется возможность создания троттлинга сети. Для этого нужно использовать [browser_set_up.py](https://github.com/PavelChuu/ForAvito-QA-test-trainee/blob/main/tests/browser_set_up.py). Настройка проходит отдельно для мобильной и desktop версией браузера.
