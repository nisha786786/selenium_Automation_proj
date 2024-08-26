from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

username = "7667684860"
driver.maximize_window()

# LOGIN
driver.get(" https://test.korangle.com:4200")
time.sleep(3)
driver.find_element(By.XPATH, '//input[@type="number"]').send_keys(username)
time.sleep(3)
driver.find_element(By.XPATH, '//a[text()="Submit"]').click()
print("successfully navigate to dashboard page")

time.sleep(3)
driver.find_element(By.XPATH,'//a[@href="/dashboard/7667684860/movie/7173"]').click()
name = driver.find_element(By.XPATH,'(//td//input[@type="text"])[1]')
description = driver.find_element(By.XPATH,'(//td//input[@type="text"])[2]')
date = driver.find_element(By.XPATH,'//td//input[@type="date"]')
time.sleep(2)
name.clear()
description.clear()
date.clear()
time.sleep(2)
name.send_keys("PK2")
description.send_keys("An alien on Earth loses the only device he can use to communicate with his spaceship")
date.send_keys("20-02-2000")
time.sleep(2)
driver.find_element(By.XPATH,'//button[text()="Edit"]').click()
time.sleep(3)
alert1 = driver.switch_to.alert
print(alert1.text)
alert1.accept()
time.sleep(2)

# DELETE MOVIE
driver.find_element(By.XPATH,'//a[@href="/dashboard/7667684860/movie-list"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//a[@href="/dashboard/7667684860/movie/7180"]').click()
delete = driver.find_element(By.XPATH,'//button[text()="Delete"]').click()