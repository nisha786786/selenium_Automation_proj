from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv
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

movielist = driver.find_element(By.XPATH, '//a[@href="/dashboard/7667684860/movie-list"]')
movielist.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//td/a')))

# Find all links in the movie table
links = driver.find_elements(By.XPATH, '//td/a')
print(len(links))


# Create an empty list to store movie data
movies = []

for i in links:
    val = i.get_attribute("href")
    print(val)
    movies.append(val)

# Save the links into a CSV file
with open('movies_links.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Movies List Links'])  # Write the header
    for val in movies:
        writer.writerow([val])





# Optional: Close the browser
driver.quit()