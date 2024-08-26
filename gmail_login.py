from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
load_dotenv()

username = os.getenv("email")
passw = os.getenv("e_password")
driver.maximize_window()
# login
driver.get("https://mail.google.com")
driver.find_element(By.ID, "identifierId").send_keys(username)
driver.find_element(By.XPATH, '//*[@id="identifierNext"]').click()
driver.implicitly_wait(6)
driver.find_element(By.NAME, "Passwd").send_keys(passw)
driver.find_element(By.XPATH, '//*[@id="passwordNext"]').click()
print("login successfully")

#  compose email
driver.find_element(By.XPATH, '//div[@role="button" and text()="Compose"]').click()  # compose email
sleep(4)

driver.find_element(By.XPATH, '//input[@aria-label="To recipients"]').send_keys(username)   # to
sleep(3)

# subject section
driver.find_element(By.XPATH, '//input[@name="subjectbox"]').send_keys("Test Mail")  # subject
sleep(4)

# write body section
driver.find_element(By.XPATH, '//div[@aria-label="Message Body"]').send_keys("Test Email Body")  # body

# click on 3 dot
driver.find_element(By.XPATH, '//div[@aria-label="More options" and @role="button"]').click()  # click on 3 dot
sleep(4)
# go to label
driver.find_element(By.XPATH, '//div[text()="Label"]').click()
sleep(3)
# mark social checkbox
driver.find_element(By.XPATH, '//div[@role="menuitemcheckbox" and @title="Social"]').click()   # click marks on social

# send message
sleep(3)
driver.find_element(By.XPATH, '//div[@role="button" and @aria-label="Send ‪(Ctrl-Enter)‬"]').click()  # send button
print("message sent successfully")
sleep(3)

# click on inbox
driver.find_element(By.XPATH, '//a[@href="https://mail.google.com/mail/u/0/#inbox"]').click()

# click on social
driver.find_element(By.XPATH, '//div[starts-with(@data-tooltip,"Messages from '
                              'social networks, media-sharing sites, online dating services, and other social websites.") '
                              'and text()="Social"]').click()
sleep(4)

driver.find_element(By.XPATH, '(//tr[@class="zA zE"])[3]').click()

sleep(4)
driver.quit()
