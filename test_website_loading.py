
import unittest
from selenium import webdriver

class TestWebsiteLoading(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "/usr/bin/google-chrome"
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://atg.world")

    def test_website_loading(self):
        expected_title = "ATG.World"
        actual_title = self.driver.title
        self.assertEqual(expected_title, actual_title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

