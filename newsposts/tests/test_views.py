from django.test import TestCase, Client
from django.shortcuts import redirect
from django.urls import reverse
from newsposts.models import NewsPost


class TestViews(TestCase):

    def setUp(self):
        self.c = Client()
        NewsPost.objects.create(
            title='PostTest1',
            content='bla bla bla',
            pk=1
        )

    def test_newsposts_GET(self):
        response = self.c.get(reverse('get_newsposts'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsposts.html')


    def test_single_articlepost_GET(self):
        response = self.c.get(reverse('news_detail', args=[1]))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'articlepost.html')

