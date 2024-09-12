from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
from concurrent.futures import ThreadPoolExecutor
import os

# URL of the website
url = 'https://iptv-nederland.com/wp-json/wp/v2/posts'

# Number of visits you want to simulate
number_of_visits = 100

# Maximum number of concurrent sessions
max_concurrent_sessions = 5

# Firefox binary location - update this to your Firefox executable path
FIREFOX_BINARY_LOCATION = r"C:\Program Files\Mozilla Firefox\firefox.exe"

# Geckodriver location - update this to your geckodriver path
GECKODRIVER_PATH = r'C:\src\firefox\geckodriver.exe'

def setup_options():
    options = Options()
    options.add_argument('-headless')  # Ensure headless mode is enabled
    options.set_preference("dom.webdriver.enabled", False)
    options.set_preference('useAutomationExtension', False)
    options.binary_location = FIREFOX_BINARY_LOCATION
    return options

def send_request(visit_number):
    options = setup_options()
    try:
        driver = webdriver.Firefox(service=Service(GECKODRIVER_PATH), options=options)
        
        # Confirm headless mode
        is_headless = driver.execute_script("return navigator.webdriver")
        if is_headless is None:
            print(f"Visit {visit_number}: Confirmed headless mode")
        else:
            print(f"Visit {visit_number}: Warning - May not be in headless mode")
        
        driver.get(url)
        print(f"Visit {visit_number}: Success")
        driver.quit()
    except WebDriverException as e:
        print(f"Visit {visit_number}: Failed with WebDriverException: {e}")
    except Exception as e:
        print(f"Visit {visit_number}: Unexpected error: {e}")

def simulate_traffic():
    with ThreadPoolExecutor(max_workers=max_concurrent_sessions) as executor:
        executor.map(send_request, range(1, number_of_visits + 1))

if __name__ == "__main__":
    if not os.path.exists(FIREFOX_BINARY_LOCATION):
        raise FileNotFoundError(f"Firefox binary not found at {FIREFOX_BINARY_LOCATION}")
    
    print("Starting traffic simulation with headless browsers...")
    simulate_traffic()
    print("Traffic simulation completed.")