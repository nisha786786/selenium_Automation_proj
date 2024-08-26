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

time.sleep(2)
# Movie list Dashboard
movielist = driver.find_element(By.XPATH,'//a[@href="/dashboard/7667684860/movie-list"]')
movielist.click()
time.sleep(3)

# Define the filter value
inputvalue = ("Kal Ho Na Ho")
# Locate the filter input field and send keys
input_filter = driver.find_element(By.XPATH,'//input[@type="text"]')
input_filter.send_keys(inputvalue)

# Wait until the filtered results are loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tr')))

# verify filter
filters = driver.find_elements(By.XPATH,'//tr')
# Assert that there is exactly one result
assert len(filters) == 1, "filter did not return expected movie"

# Verify the filter result matches the input value
for i in filters:
    val = i.text
    print(val)
    assert  inputvalue in val, "return value not match with input value"
driver.quit()