from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options (enable headless mode if needed)
options = Options()
# Uncomment the line below to run in headless mode
# options.headless = True  

# Set up the Chrome WebDriver with the appropriate driver manager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Navigate to the desired URL
driver.get("https://www.amazon.in/s?k=laptop&crid=1X1TX221T7QRB&sprefix=%2Caps%2C166&ref=nb_sb_ss_recent_1_0_recent")

try:
    # Wait for the element to be visible before interacting with it (increase wait time to 30 seconds)
    elem = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "puis-card-container"))
    )
    
    # If the element is found, print the text of the element or perform other actions
    print(elem.text)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Wait a few seconds to ensure the page is fully loaded (adjust timing if needed)
    time.sleep(2)
    
    # Close the browser session gracefully
    driver.quit()
