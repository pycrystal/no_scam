from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#https://professiyapro.store/dn_rb_admin?utm_source=google&utm_medium=denis_kz&utm_campaign=19577173562&utm_content=145374036457&utm_term=video33&gclid=CjwKCAjwrpOiBhBVEiwA_473dC3PDAaR8hrrnjV-O4JOBsWED7_gZuWTUWojlr4BoIEySmBSie_9ABoCrNkQAvD_BwE#forma
#https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html
#https://paveldmitriev.com/consultation-with-mentor
option = webdriver.FirefoxOptions()
option.set_preference("dom.webdriver.enabled", True)

driver = webdriver.Firefox(executable_path="/home/crystal/Python/selenium/driver/geckodriver", options=option)

#link = "https://professiyapro.store/dn_rb_admin?utm_source=google&utm_medium=denis_kz&utm_campaign=19577173562&utm_content=145374036457&utm_term=video33&gclid=CjwKCAjwrpOiBhBVEiwA_473dC3PDAaR8hrrnjV-O4JOBsWED7_gZuWTUWojlr4BoIEySmBSie_9ABoCrNkQAvD_BwE#forma"

try:
   driver.get(url="https://sso.teachable.com/secure/360899/identity/sign_up/email")
   driver.implicitly_wait(10)
   name = driver.find_element(By.ID, "user_name")
   driver.implicitly_wait(10)
   name.click()
   driver.implicitly_wait(10)
   name.send_keys("Мы все видим")
   driver.implicitly_wait(10)
   email = driver.find_element(By.ID, "user_email")
   driver.implicitly_wait(10)
   email.click()
   driver.implicitly_wait(10)
   email.send_keys("123456@mail.com")
   driver.implicitly_wait(10)
   password = driver.find_element(By.ID, "password")
   driver.implicitly_wait(10)
   password.click()
   driver.implicitly_wait(10)
   password.send_keys("123456")
   driver.implicitly_wait(10)
   button = driver.find_element(By.NAME, "commit")
   driver.implicitly_wait(10)
   button.click()
   time.sleep(10)

except Exception as ex:
    print(ex)

finally:
    driver.close()
    driver.quit        