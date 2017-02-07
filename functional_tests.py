from selenium import webdriver
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
        self.fail('Finish the test!')

        # You should be prompted to add a new todo list

        # Type "buy milk".


        # This should create a todo list, I suppose.
        # You click enter, the page reloads and now lists "1. buy milk".

        # You can type again. Type "make chocolate".

        # Hit enter. Page loads. "2. make chocolate" now appears.

        # You know what to do. You want to save this.
        # The page should show you a unique URL for your list.
        # Some blablabla is writen about this

        # "Let me check if this URL wor... It works!"

        # Buy! I mean, bye

        browser.quit()


if __name__ == '__main__':
    unittest.main()