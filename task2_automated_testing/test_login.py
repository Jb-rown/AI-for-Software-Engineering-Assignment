import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# Test data
test_cases = [
    {"username": "admin@example.com", "password": "admin123", "expected": "fail"},
    {"username": "", "password": "admin123", "expected": "fail"},
    
]

@pytest.mark.parametrize("case", test_cases)
def test_login(case, driver):
    driver.get("https://academy.powerlearnprojectafrica.org/login")
    wait = WebDriverWait(driver, 10)

    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    try:
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        email_input.clear()
        email_input.send_keys(case["username"])

        password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
        password_input.clear()
        password_input.send_keys(case["password"])

        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
        login_button.click()

        # Wait for login to finish
        WebDriverWait(driver, 5).until(lambda d: "dashboard" in d.current_url.lower() or "login" in d.current_url.lower())
        actual = "success" if "dashboard" in driver.current_url.lower() else "fail"

    except Exception as e:
        actual = "error"
        print(f" Error for test case {case}: {e}")
        filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{case['username'] or 'blank'}_error.png"
        driver.save_screenshot(os.path.join(screenshot_dir, filename))
        pytest.fail(f"Test crashed: {e}", pytrace=False)

    # Assertion
    try:
        assert actual == case["expected"], f"Expected {case['expected']}, got {actual}"
    except AssertionError as ae:
        filename = f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{case['username'] or 'blank'}_fail.png"
        driver.save_screenshot(os.path.join(screenshot_dir, filename))
        raise ae
