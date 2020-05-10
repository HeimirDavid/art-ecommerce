from django.test import TestCase, Client
from django.urls import reverse
from carts.models import CartItem
from products.models import Product, OriginalPainting, CollectionCategory
from carts.views import add_to_cart

class TestViews(TestCase):
    def test_get_cart_page_without_any_cart_items_redirect(self):
        page = self.client.get("/cart/")
        self.assertEquals(page.status_code, 302)
        self.assertTemplateUsed('products.html')

    """
    def test_add_item_to_cart_POST(self):
        client = Client()
        self.painting1 = OriginalPainting.objects.create(
            stock = True,
            price = 5.00,
            size = 'large',
            pk=5,
        )

        self.collection1 = CollectionCategory.objects.create(
            name = "collection1",
            description = "Some description about a cool collection",
            pk=3,
        )

        self.product1 = Product.objects.create(
            name="product1",
            description="bla bla bla",
            image="some link",
            original_painting = self.painting1,
            collection = self.collection1,
            pk=1,
        )

        response = self.client.post(reverse('add_to_cart', args=[1]))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(self.product1.first().name, 'product1')"""

