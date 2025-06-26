import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime

def test_login_page():
    test_cases = [
        {"username": "admin@example.com", "password": "admin123", "expected": "fail"},
        {"username": "", "password": "admin123", "expected": "fail"},
        
    ]

    results = []

    # Create output folders
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    results_file = f"login_test_results_{timestamp}.csv"
    screenshot_dir = "screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)

    # Write CSV header
    with open(results_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "Password", "Expected", "Actual", "Result", "Screenshot"])

        for i, case in enumerate(test_cases, start=1):
            driver = webdriver.Chrome()
            driver.get("https://academy.powerlearnprojectafrica.org/login")
            wait = WebDriverWait(driver, 10)
            screenshot_file = ""

            try:
                email_input = wait.until(EC.presence_of_element_located((By.NAME, "email")))
                email_input.clear()
                email_input.send_keys(case["username"])

                password_input = wait.until(EC.presence_of_element_located((By.NAME, "password")))
                password_input.clear()
                password_input.send_keys(case["password"])

                login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
                login_button.click()
                time.sleep(3)

                actual = "success" if "dashboard" in driver.current_url.lower() else "fail"
                result = "Pass" if actual == case["expected"] else "Fail"

                # Take screenshot on failure
                if result != "Pass":
                    screenshot_file = os.path.join(screenshot_dir, f"{i}_{case['username'] or 'blank'}_fail.png")
                    driver.save_screenshot(screenshot_file)

            except TimeoutException:
                actual = "error"
                result = "Error"
                screenshot_file = os.path.join(screenshot_dir, f"{i}_{case['username'] or 'blank'}_timeout.png")
                driver.save_screenshot(screenshot_file)

            except Exception as e:
                actual = "error"
                result = "Error"
                screenshot_file = os.path.join(screenshot_dir, f"{i}_{case['username'] or 'blank'}_exception.png")
                driver.save_screenshot(screenshot_file)
                print(f" Error on case {case}: {e}")

            finally:
                driver.quit()

            writer.writerow([case["username"], case["password"], case["expected"], actual, result, screenshot_file])
            results.append(result)

    return results, results_file

if __name__ == "__main__":
    test_results, log_file = test_login_page()
    print("Tests complete. Results logged to:", log_file)
