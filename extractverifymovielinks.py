from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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


# verify Movie list display with name description and date
movielist = driver.find_element(By.XPATH, '//a[@href="/dashboard/7667684860/movie-list"]')
movielist.click()

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//td/a')))

# Find all rows in the movie table
links = driver.find_elements(By.XPATH, '//td/a')
print("number of rows", len(links))
assert len(links) > 0, "No links found!"
time.sleep(3)

# Iterate through each row and print the text content
for i in links:
    val = i.get_attribute("href")  # Get the text content of the row
    print(val)


#
driver.quit()