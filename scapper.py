from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

driver = webdriver.Chrome()

driver.get("https://www.google.com")

try:
    # Wait for the element with name="q" to be present
    elem = WebDriverWait(driver, 2000).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    elem.send_keys("Amazon")
    elem.submit()

finally:
    time.sleep(3000)
    driver.quit()
