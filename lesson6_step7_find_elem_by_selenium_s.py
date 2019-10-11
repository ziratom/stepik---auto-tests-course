from selenium import webdriver
import time 

try: 
    #Старая страница
    link = "http://suninjuly.github.io/registration1.html"
    #Новая страница
    #link = "http://suninjuly.github.io/registration2.html"

    browser = webdriver.Chrome()
    browser.get(link)
    # Первое обязательное поле
    element = browser.find_element_by_css_selector('input[class="form-control first"][required]')
    element.send_keys("Первое обязательное поле")
    # Второе обязательное поле
    element = browser.find_element_by_css_selector('input[class="form-control second"][required]')
    element.send_keys("Второе обязательное поле")
    # Третье обязательное поле
    element = browser.find_element_by_css_selector('input[class="form-control third"][required]')
    element.send_keys("Третье обязательное поле")

    time.sleep(2)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()





