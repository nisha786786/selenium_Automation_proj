from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

# ADD MOVIES
driver.find_element(By.XPATH,'//a[text()="Add Movies"]').click()
driver.find_element(By.XPATH,'(//td//input[@type="text"])[1]').send_keys("Wake UP Sid")
driver.find_element(By.XPATH,'(//td//input[@type="text"])[2]').send_keys("A Love Sghgh")
driver.find_element(By.XPATH,'//td//input[@type="date"]').send_keys("20-02-2022")

driver.find_element(By.XPATH,'//button[text()="Add Movie"]').click()

try:
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    print("Alert text:", alert.text)  # Print the alert text
    alert.accept()  # Accept the alert
except Exception as e:
    print("No alert appeared or there was an issue:", e)

#
#alert = driver.switch_to.alert
#print(alert.text)
#alert.accept()

