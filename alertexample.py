import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = options)


driver.get("https://demo.automationtesting.in/Alerts.html")

driver.maximize_window()

driver.find_element(By.ID,'OKTab').click()
time.sleep(3)
# alert with only ok button (accept)
driver.switch_to.alert.accept()