from typing import Self
from selenium import webdriver
import unittest
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

#executable_path = r"C:\Users\Trent\AppData\Local\Mozilla Firefox\firefox.exe"
#options = selenium.webdriver.Options()
#options.binary_location = executable_path
#print(options.binary_location)
#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#browser = driver
#driver.get('http://google.com/')

#browser = webdriver.Firefox()
#browser = webdriver.Firefox(options = options)
#browser = webdriver.Firefox(executable_path=executable_path)


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # # She goes to check out its homepage.
        self.browser.get('http://localhost:8000')
        
        # She notices the page title and header mention to-do lists
        assert 'To-Do' in browser.title, "Browser title was " + browser.title

        # She is invited to enter a to-do item straight away


        # She types "Buy peacock feather" into a text box.
        # (Edith's hobby is tying fly-fishing lures.)


        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in the to-do list.


        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers tto make a fly" (Edith is very methodical.)


        # The page updates again, and now shows both items on her list.


        # Edith wonder wether the site will remember her list.
        # Then she sees that the site has generated a unique URL for her --
        # there is some explanatory text to that effect.


        # She visit that URL - her to-do list is still there.


        # Satisfied, she goes back to sleep


        




browser.quit()