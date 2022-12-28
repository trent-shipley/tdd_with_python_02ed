from django.test import LiveServerTestCase
#from typing import Self
from selenium import webdriver
from selenium.webdriver.common.by import By  # Change in Ch4 
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.common.exceptions import WebDriverException
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time
import unittest


MAX_WAIT = 10


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        
    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except(AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app.
        # # She goes to check out its homepage.
        self.browser.get(self.live_server_url)
        
        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
#        header_text = self.browser.find_element_by_tag_name('h1').text  Not working 2022-12-20
        header_text = self.browser.find_element(By.TAG_NAME,'h1').text # Selenium update
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element(By.ID, 'id_new_item')  # Selenium update
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 
            'Enter a to-do item'
        )

        # She types "Buy peacock feather" into a text box.
        # (Edith's hobby is tying fly-fishing lures.)
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in the to-do list.

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        
#        self.check_for_row_in_list_table('1: Buy peacock feathers')
        
        table = self.browser.find_element(
            By.ID, 'id_list_table'
        )  # Selenium update
        rows = table.find_elements(By.TAG_NAME, 'tr')  # Selenium update
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        
        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers tto make a fly" 
        # (Edith is very methodical.)
        
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        
        # The page updates again, and now shows both items on her list.
        
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
        
        # Edith wonder wether the site will remember her list.
        # Then she sees that the site has generated a unique URL for her --
        # there is some explanatory text to that effect.

        self.fail('Finish the test!')

        # She visit that URL - her to-do list is still there.


        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')

