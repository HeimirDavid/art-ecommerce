from django.test import TestCase
from django.urls import reverse, resolve
from newsposts.views import get_newsposts, news_detail

class TestUrls(TestCase):
    """
    Simple test to see if the ulrs resolves,
    source: https://www.youtube.com/watch?v=0MrgsYswT1c&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=2
    """
    def test_get_newsposts_url_is_resolved(self):
        url = reverse('get_newsposts')
        print(resolve(url))
        self.assertEquals(resolve(url).func, get_newsposts)


    def test_news_detail_url_resolves(self):
        url = reverse('news_detail', args=['1']) #expects some number
        self.assertEquals(resolve(url).func, news_detail)