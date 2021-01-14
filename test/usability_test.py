from selenium import webdriver

import unittest
class UsabilityTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome()
    def tearDown(self):
        self.browser.quit()

    def test_can_open_and_if_title(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('To-Do', self.browser.title)

