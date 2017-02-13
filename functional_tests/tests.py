from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Open this new todo list web page
        self.browser.get(self.live_server_url)

        # The titles tell me what the site is: a Todo list site
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # You should be prompted to add a new todo list
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Type "buy milk".
        inputbox.send_keys('buy milk')

        # This should create a todo list, I suppose.
        # You click enter, the page reloads and now lists "1. buy milk".
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.check_for_row_in_list_table('1. buy milk')

        # You can type again. Type "make chocolate".
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('make chocolate')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # Hit enter. Page loads. "2. make chocolate" now appears.
        self.check_for_row_in_list_table('1. buy milk')
        self.check_for_row_in_list_table('2. make chocolate')
        # You know what to do. You want to save this.
        # The page should show you a unique URL for your list.
        # Some blablabla is writen about this
        self.fail('finish test')

        # "Let me check if this URL wor... It works!"
