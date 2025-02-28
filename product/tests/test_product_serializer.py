from django.test import TestCase

from product.serializers import ProductSerializer
from product.factories import ProductFactory, CategoryFactory


class TestProductSerializer(TestCase):
	def setUp(self):
		# data = {
		# 	"title": "Vidas Secas", 
		# 	"price":50, 
		# 	"category":None
		# }

		self.category = CategoryFactory(title="literatura brasileira", slug="literatura do Brasil", description="literatura brasileira", active=True)
		self.product = ProductFactory(
			title="Vidas Secas", 
			description="blablabla",
			price=50, 
			active=True,
			category=[self.category]
			)
		self.product_serializer = ProductSerializer(self.product)

	def test_product_serializer(self):
		serializer_data = self.product_serializer.data
		self.assertEqual(serializer_data["title"], "Vidas Secas")
		self.assertEqual(serializer_data["price"], 50)
		self.assertEqual(serializer_data["category"][0]["title"], "literatura brasileira")

