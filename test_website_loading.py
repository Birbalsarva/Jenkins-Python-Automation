import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestWebsiteLoading(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run in headless mode (no GUI)
        chrome_options.add_argument('--no-sandbox')  # Required for running as root user
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        
    def test_website_loads(self):
        self.driver.get("https://atg.world")  # Replace with your website URL
        
        # Check if the website title contains "ATG"
        self.assertIn("ATG", self.driver.title)
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

