import unittest
from selenium import webdriver

class WebsiteLoadingTest(unittest.TestCase):
    def setUp(self):
        # Set up the browser instance (assuming you have the WebDriver executable in PATH)
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Close the browser instance after the test completes
        self.driver.quit()

    def test_website_loading(self):
        # Replace 'https://www.example.com' with the actual URL you want to test
        url = 'https://atg.world/'

        self.driver.get(url)

        # Check if the page title exists to determine if the website is loading properly
        page_title = self.driver.title

        # Assert whether the page title exists or not
        if page_title:
            self.assertEqual(page_title, 'Across The Globe (ATG) - Professional and Personal Social Networking')
            print("Pass: The website is loading.")
        else:
            self.fail("Fail: The website is not loading.")

if __name__ == '__main__':
    unittest.main()
