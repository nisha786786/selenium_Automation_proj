from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tr')))
# get lenght of movies before adding
before_add = driver.find_elements(By.XPATH,'//tr')
print("number of rows movies before adding" ,len(before_add))

# ADD MOVIES
driver.find_element(By.XPATH,'//a[text()="Add Movies"]').click()
driver.find_element(By.XPATH,'(//td//input[@type="text"])[1]').send_keys("evil dead")
driver.find_element(By.XPATH,'(//td//input[@type="text"])[2]').send_keys("evil dead")
driver.find_element(By.XPATH,'//td//input[@type="date"]').send_keys("20-02-2022")

driver.find_element(By.XPATH,'//button[text()="Add Movie"]').click()
time.sleep(3)

alert = driver.switch_to.alert
alerttext = alert.text
print(alerttext)
alert.accept()  # Accept the alert

# to verify click on Movie list Dashboard
driver.find_element(By.XPATH,'//a[@href="/dashboard/7667684860/movie-list"]').click()
# load list of movies
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tr')))

after_add = driver.find_elements(By.XPATH,'//tr')
print("number of movies row after adding:",len(after_add))
assert len(after_add) == len(before_add) + 1,'movie  did not add correctly'