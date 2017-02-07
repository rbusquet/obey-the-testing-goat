from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Open this new todo list web page
        self.browser.get('http://localhost:8000')

        # The titles tell me what the site is: a Todo list site
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # You should be prompted to add a new todo list
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a todo-item'
        )

        # Type "buy milk".
        inputbox.send_keys('buy milk')

        # This should create a todo list, I suppose.
        # You click enter, the page reloads and now lists "1. buy milk".
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.test == '1. buy milk' for row in rows)
        )

        # You can type again. Type "make chocolate".
        self.fail('Finish test')

        # Hit enter. Page loads. "2. make chocolate" now appears.

        # You know what to do. You want to save this.
        # The page should show you a unique URL for your list.
        # Some blablabla is writen about this

        # "Let me check if this URL wor... It works!"

        # Buy! I mean, bye

        browser.quit()


if __name__ == '__main__':
    unittest.main()