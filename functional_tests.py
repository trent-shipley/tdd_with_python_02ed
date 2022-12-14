from selenium import webdriver
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

#executable_path = r"C:\Users\Trent\AppData\Local\Mozilla Firefox\firefox.exe"
#options = selenium.webdriver.Options()
#options.binary_location = executable_path
#print(options.binary_location)
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#driver.get('http://google.com/')

#browser = webdriver.Firefox()
#browser = webdriver.Firefox(options = options)
#browser = webdriver.Firefox(executable_path=executable_path)
driver.get('http://127.0.0.1:8000')

assert 'Django' in browser.title