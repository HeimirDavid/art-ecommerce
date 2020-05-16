from django.test import TestCase
from django.urls import reverse, resolve
from carts.views import view_cart, add_to_cart, remove_from_cart, clear_cart


class TestUrls(TestCase):
    """
    Simple test to see if the ulrs resolves,
    source: https://www.youtube.com/watch?v=0MrgsYswT1c&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=2
    """
    def test_view_cart_url_resolves(self):
        url = reverse('view_cart')
        self.assertEquals(resolve(url).func, view_cart)


    def test_add_to_cart_url_resolves(self):
        url = reverse('add_to_cart', args=['1']) #expects some number
        self.assertEquals(resolve(url).func, add_to_cart)


    def test_remove_from_cart_url_resolves(self):
        url = reverse('remove_from_cart', args=['1']) #expects some number
        self.assertEquals(resolve(url).func, remove_from_cart)


    def test_clear_cart_url_resolves(self):
        url = reverse('clear_cart') #expects some number
        self.assertEquals(resolve(url).func, clear_cart)