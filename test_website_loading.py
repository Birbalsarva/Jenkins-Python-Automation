import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestWebsiteLoading(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--remote-debugging-address=0.0.0.0")
        chrome_options.add_argument("--remote-debugging-port=9222")
        self.driver = webdriver.Chrome(options=chrome_options, executable_path="/usr/local/bin/chromedriver")
        self.driver.get("https://atg.world")

    def test_website_loading(self):
        expected_title = "Across The Globe (ATG) - Professional and Personal Social Networking"
        actual_title = self.driver.title
        self.assertEqual(expected_title, actual_title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
