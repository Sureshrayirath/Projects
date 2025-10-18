from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Step 1: Set up the browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/login")

# Step 2: Log in to LinkedIn
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("Enter your linkedin email")  # Replace with your LinkedIn email
password.send_keys("Enter your password here")              # Replace with your LinkedIn password

# Click login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()
time.sleep(3)

# Step 3: Search for profiles using the correct class name for search box
search_box = driver.find_element(By.CSS_SELECTOR, ".search-global-typeahead__input.search-global-typeahead__input--ellipsis")
search_box.send_keys("Software Engineer")  # Replace with your search query
search_box.send_keys(Keys.RETURN)
time.sleep(5)

# Step 4: Navigate to the "People" tab using Explicit Wait
try:
    # Wait for the "People" button to be clickable
    people_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'People')]"))
    )
    people_tab.click()
    print("Navigated to the 'People' section successfully.")
    time.sleep(5)
except Exception as e:
    print(f"Error navigating to the 'People' section: {e}")
    driver.quit()
    exit()

# Step 5: Send connection requests
try:
    while True:  # Loop to process profiles on the current page
        # Scroll to load profiles dynamically
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)  # Wait for new profiles to load

        # Find all "Connect" buttons
        connect_buttons = driver.find_elements(By.XPATH, "//button[.//span[contains(@class, 'artdeco-button__text') and text()='Connect']]")

        if not connect_buttons:
            print("No 'Connect' buttons found on the current page.")
            break  # Exit the loop if no buttons are found

        for button in connect_buttons:
            try:
                # Scroll to the "Connect" button to bring it into view
                driver.execute_script("arguments[0].scrollIntoView(true);", button)
                time.sleep(1)  # Allow time for scrolling

                # Try normal click
                try:
                    button.click()
                except:
                    # Fallback to JavaScript click if intercepted
                    driver.execute_script("arguments[0].click();", button)

                time.sleep(2)  # Allow time for the pop-up to load

                # Click the "Send without a note" button in the pop-up
                try:
                    send_without_note_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[.//span[contains(@class, 'artdeco-button__text') and text()='Send without a note']]"))
                    )
                    send_without_note_button.click()
                    print("Connection request sent successfully.")
                    time.sleep(2)
                except Exception as send_error:
                    print(f"Error finding 'Send without a note' button: {send_error}")

            except Exception as button_error:
                print(f"Error clicking 'Connect' button: {button_error}")

except KeyboardInterrupt:
    print("Script stopped by user.")
