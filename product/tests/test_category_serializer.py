from django.test import TestCase

from product.factories import ProductFactory, CategoryFactory
from product.serializers import CategorySerializer


class TestCategorySerializer(TestCase):
	def setUp(self):
		self.category = CategoryFactory(
			title="Literatura brasileira",
			slug="Literatura brasileira",
			description="livros de literatura do Brasil",
			active=True
		)
		self.category_serializer = CategorySerializer(self.category)

	def test_category_serializer(self):
		serializer_data = self.category_serializer.data

		self.assertEqual(serializer_data["title"], "Literatura brasileira")
		self.assertEqual(serializer_data["slug"], "Literatura brasileira")
		self.assertEqual(serializer_data["description"], "livros de literatura do Brasil")
		self.assertEqual(serializer_data["active"], True)
