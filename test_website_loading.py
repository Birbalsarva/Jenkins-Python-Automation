from selenium import webdriver
import unittest

class TestWebsiteLoading(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_website_loading(self):
        self.driver.get("https://atg.world")
        self.assertEqual("ATG - Art & Technology Group", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

