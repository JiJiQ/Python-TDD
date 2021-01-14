from selenium import webdriver
import unittest

class NewViewerTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome(executable_path="D:\\TDD\\test\\chromedriver.exe")
    def tearDown(self):
        self.browser.quit()
    def test_test1(self):
        self.browser.get("http://localhost:80")
        self.assertIn('To-Do lists',self.browser.title)
        self.fail("Finish test")
if __name__=='__main__':
    unittest.main()