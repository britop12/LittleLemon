from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def test_getall(self):
        Menu.objects.create(title='test', price=10, inventory=10)
        Menu.objects.create(title='test2', price=10, inventory=10)
        queryset = Menu.objects.all()
        self.assertEqual(queryset.count(), 2)
