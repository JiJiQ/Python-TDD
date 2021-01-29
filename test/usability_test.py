from selenium import webdriver
import time
import unittest
MAX_WAIT=10
def wait(fn):
    start_time=time.time()
    def modified_fn(*args,**kwargs):
        while True:
            try:
                return fn(*args,**kwargs)
            except AssertionError as e:
                if time.time()-start_time>MAX_WAIT:
                    raise e
                time.sleep(1)
                print('等待正确结果。。。')
    return modified_fn
class UsabilityTest(unittest.TestCase):
    def setUp(self):
        print('unittest start')
        # self.browser=webdriver.Chrome()
    def tearDown(self):
        # self.browser.quit()
        print('unittest quit')

    def test_can_open_and_if_title(self):
        self.browser.get("http://localhost:8000")
        self.assertIn('To-Do', self.browser.title)
    @wait
    # 等价于：wait_for=wait(wait_for)
    def wait_for(self,fn):
        fn()

    def wait_for1(self,fn):
        fn()
    wait_for1=wait(wait_for1)
    def test_wait_for(self):
        self.wait_for1(lambda : self.assertEqual(1,2))
