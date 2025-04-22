from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Set up Chrome options (enable headless mode if needed)
options = Options()
# Uncomment the line below to run in headless mode
# options.headless = True  

# Set up the Chrome WebDriver with the appropriate driver manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Search Query
q1 = "Mobile"

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

file = 0  # File counter

for i in range(1, 5):
    # Navigate to the desired URL
    url = f"https://www.shopsy.in/search?q={q1}&as=on&as-show=on&page={i}"
    driver.get(url)
    
    try:
        # Wait for elements to load
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "css-175oi2r")) 
        )

        # Find all elements with the given class
        elems = driver.find_elements(By.CLASS_NAME, "css-175oi2r")
        
        for elem in elems:
            d = elem.get_attribute("outerHTML")  # Fix attribute name
            
            with open(f"data/{q1}_{file}.html", "w", encoding="utf-8") as f:
                f.write(d)  # Fix method name
            
            file += 1  # Increment file count

    except Exception as e:
        print(f"An error occurred on page {i}: {e}")

    # Wait before loading the next page (to prevent being blocked)
    time.sleep(2)

# Close the browser session gracefully
driver.quit()
