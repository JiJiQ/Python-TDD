from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page
# Create your tests here.
class SmokeTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found=resolve("/")
        self.assertEqual(found.func,home_page)
    def test_home_page_return_correct_html(self):
        request=HttpRequest()
        reponse=home_page(request)
        html=reponse.content.decode('utf-8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>',html)
        self.assertTrue(html.strip().endswith('</html>'))
    def test_home_page_returns_correct_html(self):
        # request=HttpRequest()
        # response=home_page(request)
        # html=response.content.decode('utf8')
        # expected_html=render_to_string('home.html')
        # self.assertEqual(html,expected_html)
        #同时完成了root_url_resolves_to_home_page_view和home_page_return_correct_html
        response=self.client.get('/')
        html=response.content.decode('utf8')
        self.assertTemplateUsed(response,'wrong.html')