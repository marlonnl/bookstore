from django.test import TestCase

from product.factories import ProductFactory
from order.factories import OrderFactory
from order.serializers import OrderSerializer

class TestOrderSerializer(TestCase):
	def setUp(self):
		self.product1 = ProductFactory()
		self.product2 = ProductFactory()

		self.order = OrderFactory(product=(self.product1, self.product2))
		self.order_serializer = OrderSerializer(self.order)

	def test_order_serializer(self):
		serializer_data = self.order_serializer.data

		self.assertEqual(serializer_data["product"][0]["title"], self.product1.title)
		self.assertEqual(serializer_data["product"][0]["price"], self.product1.price)

		self.assertEqual(serializer_data["product"][1]["title"], self.product2.title)
		self.assertEqual(serializer_data["product"][1]["price"], self.product2.price)