from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="Ice cream", price=4, inventory=100)
        self.item2 = Menu.objects.create(title="Burger", price=8, inventory=50)

    def test_getall(self):
        item1 = MenuSerializer(Menu.objects.get(title="Ice cream"))
        item2 = MenuSerializer(Menu.objects.get(title="Burger"))

        self.assertEqual(str(item1.instance), "Ice cream : 4.00")
        self.assertEqual(str(item2.instance), "Burger : 8.00")
