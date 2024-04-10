from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Define the URL of your Flask application
URL = 'http://44.202.166.8:5000/'  

# Define test cases
def test_homepage():
    driver = webdriver.Chrome()
    driver.get(URL)

    # Example test: Check if the homepage contains expected text
    assert "Welcome to My Flask App" in driver.title

    driver.quit()

# Define additional test cases as needed

# Run the test cases
if __name__ == "__main__":
    test_homepage()
