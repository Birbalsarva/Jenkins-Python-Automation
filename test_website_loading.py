import unittest
from selenium import webdriver

class TestWebsiteLoading(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "/usr/bin/google-chrome"  # Update with the correct path
        chrome_options.add_argument("--headless")  # Add this line for headless mode
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://atg.world")

    def test_website_loading(self):
        expected_title = "Across The Globe (ATG) - Professional and Personal Social Networking"  # Updated expected title
        actual_title = self.driver.title
        self.assertEqual(expected_title, actual_title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

