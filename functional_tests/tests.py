from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
import time
import unittest

MAX_WAIT = 10
class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_for_one_user(self):

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
        # You click enter, the page reloads and now lists "1: buy milk".
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: buy milk')

        # You can type again. Type "make chocolate".
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('make chocolate')
        inputbox.send_keys(Keys.ENTER)

        # Hit enter. Page loads. "2: make chocolate" now appears.
        self.wait_for_row_in_list_table('1: buy milk')
        self.wait_for_row_in_list_table('2: make chocolate')
    
    def test_multiple_users_can_start_lists_at_different_urls(self):
        # Start new todo list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        # this should show a new url
        your_list_url = self.browser.current_url
        self.assertRegex(your_list_url, '/lists/.+')

        # new person test the url
        ## clear browser
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # they visit homepage, no sign of your list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        person_list_url = self.browser.current_url
        self.assertRegex(person_list_url, '/lists/.+')
        self.assertNotEqual(person_list_url, your_list_url)

        # Again, there is no trace of your's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

    def test_layout_and_styling(self):
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2 ,
            512,
            delta=5)

        # She starts a new list and sees the input is nicely
        # centered there too
        inputbox.send_keys('testing')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: testing')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta=5
        )

