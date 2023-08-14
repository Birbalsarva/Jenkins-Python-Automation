import unittest
from selenium import webdriver

class TestWebsiteLoading(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='/path/to/chromedriver') # Update with your ChromeDriver path
    
    def test_website_loads(self):
        self.driver.get('https://atg.world')
        title = self.driver.title
        self.assertIn('ATG World', title)  # Change this based on the expected title of the website
        
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

