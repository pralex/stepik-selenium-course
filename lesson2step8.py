from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'bio.txt')           # добавляем к этому пути имя файла 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input = browser.find_element_by_css_selector("[placeholder='Enter first name']")
    input.send_keys("Vasily")    
    
    input = browser.find_element_by_css_selector("[placeholder='Enter last name']")
    input.send_keys("Pupkin")  

    input = browser.find_element_by_css_selector("[placeholder='Enter email']")
    input.send_keys("vasily.pupkin@mail.ru")  

    input = browser.find_element_by_css_selector("#file")
    input.send_keys(file_path)  
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()