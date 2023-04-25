from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from multiprocessing import Pool
import random

link = ["https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email","https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email","https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email","https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email","https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email","https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email","https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email", "https://sso.teachable.com/secure/360899/identity/sign_up/email"]
names = ["Леша", "Илья", "Мария", "Вова", "Арсений", "Женя", "Саша", "Анна", "Галя", "Мария", "Александр", "Alex", "Ольга", "Владимир", "Богдан", "Григорий", "Наталья", "Милана", "Татьяна", "Василий", "Петя", "Николай", "Таня"]

def no_scam(link):
    try:
        option = webdriver.FirefoxOptions()
        option.headless = True

        driver = webdriver.Firefox(executable_path="/home/crystal/Python/selenium/driver/geckodriver", options=option)

        driver.get(url=link)
        driver.implicitly_wait(10)
        print("Перешел по ссылке")
        name = driver.find_element(By.ID, "user_name")
        #print("Нашел имя")
        driver.implicitly_wait(10)
        name.click()
        #print("Жмякнул")
        driver.implicitly_wait(10)
        name.send_keys(random.choice(names))
        print("Ввел имя")
        driver.implicitly_wait(10)
        email = driver.find_element(By.ID, "user_email")
        #print("Нашел почту")
        driver.implicitly_wait(10)
        email.click()
        #print("Жмякнул")
        driver.implicitly_wait(10)
        email.send_keys(f"{random.randint(1, 99999)}@mail.com")
        print("Ввел почту")
        driver.implicitly_wait(10)
        password = driver.find_element(By.ID, "password")
        #print("Нашел пароль")
        driver.implicitly_wait(10)
        password.click()
        #print("Жмякнул")
        driver.implicitly_wait(10)
        password.send_keys(random.randint(999999, 99999999))
        print("Ввел пароль")
        driver.implicitly_wait(10)
        button = driver.find_element(By.NAME, "commit")
        #print("Нашел кнопку")
        driver.implicitly_wait(10)
        button.click()
        print("Отправил")
        driver.implicitly_wait(10)
        print("-----------------")

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit()        \

p = Pool(processes=3)
p.map(no_scam, link)        
