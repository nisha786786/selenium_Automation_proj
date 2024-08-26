from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
load_dotenv()

username = os.getenv("number")
driver.maximize_window()

# LOGIN
driver.get(" https://test.korangle.com:4200")
time.sleep(3)
driver.find_element(By.XPATH, '//input[@type="number"]').send_keys(username)
time.sleep(2)
driver.find_element(By.XPATH, '//a[text()="Submit"]').click()
print("successfully navigate to dashboard page")


# Movie list display with name description and date
driver.find_element(By.XPATH, '//a[@href="/dashboard/7667684860/movie-list"]').click()
time.sleep(3)

# Filter movie with movie name
input_filter = driver.find_element(By.XPATH, '//input[@type="text"]')
time.sleep(3)
input_filter.send_keys("Kal Ho Na Ho")
time.sleep(3)

# ADD MOVIES
driver.find_element(By.XPATH, '//a[text()="Add Movies"]').click()
driver.find_element(By.XPATH, '(//td//input[@type="text"])[1]').send_keys("automationtest3")
driver.find_element(By.XPATH, '(//td//input[@type="text"])[2]').send_keys("testing with automate process")
driver.find_element(By.XPATH, '//td//input[@type="date"]').send_keys("20-08-2024")
time.sleep(2)
driver.find_element(By.XPATH, '//button[text()="Add Movie"]').click()
time.sleep(3)
alert = driver.switch_to.alert
print(alert.text)
alert.accept()  # Accept the alert
time.sleep(3)

# Edit MOVIE
driver.find_element(By.XPATH, '//a[@href="/dashboard/7667684860/movie-list"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//a[@href="/dashboard/7667684860/movie/7173"]').click()
name = driver.find_element(By.XPATH, '(//td//input[@type="text"])[1]')
description = driver.find_element(By.XPATH, '(//td//input[@type="text"])[2]')
date = driver.find_element(By.XPATH, '//td//input[@type="date"]')
time.sleep(3)
name.clear()
description.clear()
date.clear()
time.sleep(3)
name.send_keys("PK2")
description.send_keys("An alien on Earth loses the only device he can use to communicate with his spaceship")
date.send_keys("20-02-2001")
time.sleep(3)
driver.find_element(By.XPATH, '//button[text()="Edit"]').click()
time.sleep(3)
alert1 = driver.switch_to.alert
print(alert1.text)
alert1.accept()
time.sleep(3)

# DELETE MOVIE
driver.find_element(By.XPATH, '//a[@href="/dashboard/7667684860/movie-list"]').click()
time.sleep(3)
driver.find_element(By.XPATH, '//a[@href="/dashboard/7667684860/movie/7180"]').click()
driver.find_element(By.XPATH, '//button[text()="Delete"]').click()
# verifying movie details are deleted or not


driver.quit()