from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from fake_useragent import UserAgent
from multiprocessing import Pool


link = ["https://paveldmitriev.com/consultation-with-mentor"]



def no_scam(link):
    try:
        user_agents = UserAgent()

        options = webdriver.FirefoxProfile()
        options.set_preference("general.useragent.override", user_agents.random)

        option = webdriver.FirefoxOptions()
        option.headless = True 


        driver = webdriver.Firefox(executable_path = "/home/crystal/Python/selenium/driver/geckodriver", firefox_profile=options, options=option)

        for_names = ["Леша", "Илья", "Мария", "Вова", "Арсений", "Женя", "Саша", "Анна", "Галя", "Мария", "Александр", "Alex", "Ольга", "Владимир", "Богдан", "Григорий", "Наталья", "Милана", "Татьяна", "Василий", "Петя", "Николай", "Таня"]
        
        ful_name = ["Барсукевич", "Наумовец", "Лайша", "Дежко", "Тенюшко", "Кирейко", "Толмач", "Руснак", "Богданович", "Иотченко", "Качур", "Адамович", "Дубко", "Брищук", "Бародич", "Логиш", "Брейко", "Шамрук", "Турович", "Чугур", "Чудук", "Васильевич", "Ванкевич", "Михальчик", "Демидович", "Данилевич"]
        
        for_email = ["Money","cook", "kype","lave", "kenia","armenia", "ryka","pyrga", "zxc","xyz", "dygin","tyrkin", "felix","opendix", "fol","bolkon", "akyla","gunpyla", "vid","kit","jir","pir", "lada","vesta", "rebyt","ebyt", "level","penal", "gorka","porka", "dora","dyra", "vika","lipa", "vishna","filka", "gayka","reyka", "nidshe","vichka", "faster","golem", "ega","digga", "pyli","duni"]
        
        for_email2 = ["@gmail.com", "@mail.com"]

        for_numbers = ["44", "29", "25", "33"]

        for_hobby = ["Разбираюсь в криптовалюте.", "Разбираюсь во фрилансе.", "Являюсь телеграм адмистратором.", "Зарабатываю продажей машин.", "Секретарь небольшой фирмы.", "Разбираюсь в предсказаниях.", "Разбираюсь в компьютерах." ]
        
        for_problems = ["Не умею продавать. Не знаю как привлекать клиентов.", "Деньги не приходят, а лишь уходят.", "Не уверен, что это мое призвание.", "Даже не знаю в чем проблема.", "Уверен что могу лучше но не знаю как улучшаться."]

        driver.get(url=link)
        print("Открыл сайт")
        driver.implicitly_wait(10)
        name = driver.find_element(By.ID, "input_1527153268120")
        driver.implicitly_wait(10)
        name.click()
        driver.implicitly_wait(10)
        name.send_keys(f"{random.choice(for_names)} {random.choice(ful_name)}")
        driver.implicitly_wait(10)
        name.send_keys(Keys.ENTER)
        driver.implicitly_wait(10)
        email = driver.find_element(By.ID, "input_1528364085031")
        driver.implicitly_wait(10)
        email.click()
        driver.implicitly_wait(10)
        email.send_keys(f"{random.randint(1, 99999)}{random.choice(for_email)}{random.randint(1, 999)}{random.choice(for_email2)}")
        driver.implicitly_wait(10)
        email.send_keys(Keys.ENTER)
        driver.implicitly_wait(10)
        where_call = driver.find_elements(By.CLASS_NAME, "t-radio__indicator")
        driver.implicitly_wait(10)
        where_call[1].click()
        for_click = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div/div[3]/button[2]")
        driver.implicitly_wait(10)
        for_click.click()
        driver.implicitly_wait(10)
        number = driver.find_element(By.NAME, "tildaspec-phone-part[]")
        driver.implicitly_wait(10)
        number.click()
        driver.implicitly_wait(10)
        number.send_keys(f"{random.choice(for_numbers)}{random.randrange(1111111, 9999999)}")
        driver.implicitly_wait(10)
        number.send_keys(Keys.ENTER)
        driver.implicitly_wait(10)
        hobby = driver.find_element(By.ID, "input_1527252219292")
        driver.implicitly_wait(10)
        hobby.click()
        driver.implicitly_wait(10)
        hobby.send_keys(f"{random.choice(for_hobby)}")
        driver.implicitly_wait(10)
        for_click.click()
        driver.implicitly_wait(10)
        where_call[3].click()
        driver.implicitly_wait(10)
        for_click.click()
        driver.implicitly_wait(10)
        dohod = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div/div[2]/form/div[2]/div[7]/div[2]/div[1]/label[2]/div")
        driver.implicitly_wait(10)
        dohod.click()
        driver.implicitly_wait(10)
        for_click.click()
        driver.implicitly_wait(10)
        cash = driver.find_element(By.ID, "input_1613770310557")
        driver.implicitly_wait(10)
        cash.click()
        driver.implicitly_wait(10)
        cash.send_keys("1500")
        driver.implicitly_wait(10)
        cash.send_keys(Keys.ENTER)
        driver.implicitly_wait(10)
        problem = driver.find_element(By.ID, "input_1613770406340")
        driver.implicitly_wait(10)
        problem.click()
        driver.implicitly_wait(10)
        problem.send_keys(f"{random.choice(for_problems)}")
        driver.implicitly_wait(10)
        for_click.click()
        driver.implicitly_wait(10)
        how_pay = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div/div[2]/form/div[2]/div[10]/div[3]/div[1]/label[1]/div")
        driver.implicitly_wait(10)
        how_pay.click()
        driver.implicitly_wait(10)
        for_click.click()
        yes_no = driver.find_element(By.ID, "input_1616171077945")
        driver.implicitly_wait(10)
        yes_no.click()
        driver.implicitly_wait(10)
        yes_no.send_keys("Да")
        driver.implicitly_wait(10)
        yes_no.send_keys(Keys.ENTER)
        driver.implicitly_wait(10)
        where_know = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div/div[2]/form/div[2]/div[12]/div[2]/div[1]/label[4]/div")
        driver.implicitly_wait(10)
        where_know.click()
        driver.implicitly_wait(10)
        special_click = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div/div[3]/button[3]")
        driver.implicitly_wait(10)
        special_click.click()
        driver.implicitly_wait(10)
        special_click2 = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/div/div/div/div[2]/form/div[2]/div[15]/button")
        driver.implicitly_wait(10)
        special_click2.click()
        print("Разнес сайт")
        driver.implicitly_wait(10)

    except Exception as ex:
        print(ex)

    finally:
        driver.close()
        driver.quit        

p = Pool(processes=3)
p.map(no_scam, link*1000) 
