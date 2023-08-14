from selenium import webdriver

class TestWebsiteLoading(unittest.TestCase):
    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--remote-debugging-address=0.0.0.0')
        chrome_options.add_argument('--remote-debugging-port=9222')
        self.driver = webdriver.Chrome(options=chrome_options)

    # Rest of your test methods

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
