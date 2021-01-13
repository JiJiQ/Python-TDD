from selenium import webdriver

options=webdriver.ChromeOptions()
browser=webdriver.Chrome(executable_path="D:\\TDD\\test\\chromedriver.exe")

browser.get("http://localhost:80")

assert 'Django' in browser.title
browser.quit()