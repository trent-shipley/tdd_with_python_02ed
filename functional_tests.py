#from typing import Self
from selenium import webdriver
from selenium.webdriver.common.by import By  # Change in Ch4 
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time
import unittest

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

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # # She goes to check out its homepage.
        self.browser.get('http://localhost:8000')
        
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
#        header_text = self.browser.find_element_by_tag_name('h1').text  Not working 2022-12-20
        header_text = self.browser.find_element(By.TAG_NAME,'h1').text # Selenium update
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, 'id_new_item')  # Selenium update
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        

        # She types "Buy peacock feather" into a text box.
        # (Edith's hobby is tying fly-fishing lures.)
        inputbox.send_keys('Buy peacock feathers')


        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in the to-do list.
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table = self.browser.find_element(
            By.ID, 'id_list_table')  # Selenium update
        rows = table.find_elements(By.TAG_NAME, 'tr')  # Selenium update
        self.assertTrue(
            any(row.next=='1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )
        
        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers tto make a fly" (Edith is very methodical.)
        
        self.fail('Finish the test!')


        # The page updates again, and now shows both items on her list.


        # Edith wonder wether the site will remember her list.
        # Then she sees that the site has generated a unique URL for her --
        # there is some explanatory text to that effect.


        # She visit that URL - her to-do list is still there.


        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')

