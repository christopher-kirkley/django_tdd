from selenium import webdriver

browser = webdriver.Firefox(executable_path = '/Users/ck/python/geckodriver/geckodriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
