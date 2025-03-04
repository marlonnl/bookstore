import json

from rest_framework.test import APIClient, APITestCase
from rest_framework.views import status

from django.urls import reverse

from product.factories import CategoryFactory
from product.models import Category


class CategoryViewSet(APITestCase):
	client = APIClient()

	def setUp(self):
		self.category = CategoryFactory(title="books")
		
	def test_get_all_categories(self):
		response = self.client.get(
			reverse("category-list", kwargs={ "version": "v1" })
		)

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		category_data = json.loads(response.content)

		# print("data ", category_data)
		self.assertEqual(category_data["results"][0]["title"], self.category.title)

	def test_create_category(self):
		data = json.dumps({
			"title": "literatura",
		})

		response = self.client.post(
			reverse("category-list", kwargs={ "version": "v1" }),
			data=data,
			content_type="application/json"
		)

		# import pdb; pdb.set_trace()

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		created_category = Category.objects.get(title="literatura")
		
		self.assertEqual(created_category.title, "literatura")