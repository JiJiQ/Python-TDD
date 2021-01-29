from .base import FunctionalTest
class MyListsTest(FunctionalTest):

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        self.browser.get(self.live_server_url)
        self.add_lists_item('Reticulate splines')
        self.add_lists_item('Immanentize eschaton')
        first_list_url=self.browser.current_url

        self.browser.find_element_by_link_text('My lists').click()

        self.wait_for(lambda : self.browser.find_element_by_link_text('Reticulate splines'))
        self.browser.get(self.live_server_url)
        self.add_lists_item('Click cows')
        second_list_url=self.browser.current_url

        self.browser.find_element_by_link_text('My lists').click()
        self.wait_for(lambda : self.browser.find_element_by_link_text('Click cows'))
        self.browser.find_element_by_link_text('Click cows').click()
        self.wait_for(lambda : self.assertEqual(self.browser.current_url,second_list_url))
        self.browser.find_element_by_link_text('Log out').click()
        self.wait_for(lambda : self.assertEqual(self.browser.find_elements_by_link_text('My lists'),[]))
    def test_show_no_list_if_not_log_in(self):
        self.browser.get(self.live_server_url)
        self.add_lists_item('item1')
        self.browser.find_element_by_link_text('My lists').click()
        url=self.browser.current_url
        self.browser.find_element_by_link_text('Log out').click()
        self.browser.get(url)
        self.wait_for(lambda : self.assertNotIn('item1',self.browser.find_element_by_tag_name('body').text))
    def test_show_no_item_if_not_log_in(self):
        self.browser.get(self.live_server_url)
        self.add_lists_item('item1')
        url=self.browser.current_url
        self.browser.find_element_by_link_text('Log out').click()
        self.browser.get(url)
        self.wait_for(lambda : self.assertNotIn('1:item1',self.browser.find_element_by_tag_name('body').text))