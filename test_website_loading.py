import unittest
from selenium import webdriver

class TestWebsiteLoading(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "/usr/bin/google-chrome"  # Replace with your actual path to Chrome binary
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=chrome_options)
        self.driver.get("https://atg.world")

    def test_website_loading(self):
        expected_title = "Across The Globe (ATG) - Professional and Personal Social Networking"
        actual_title = self.driver.title
        self.assertEqual(expected_title, actual_title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


