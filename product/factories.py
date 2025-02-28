import factory

from product.models import Product
from product.models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
	title = factory.Faker('pystr')
	slug = factory.Faker('pystr')
	description = factory.Faker('pystr')
	active = factory.Iterator([True, False])

	class Meta:
		model = Category


class ProductFactory(factory.django.DjangoModelFactory):
	title = factory.Faker('pystr')
	price = factory.Faker('pyint')
	category = factory.LazyAttribute(CategoryFactory) # pode ser blank
	
	@factory.post_generation
	def category(self, create, extracted, **kwargs):
		if not create:
			return

		# caso tenha sido declarada alguma categoria
		if extracted:
			for category in extracted:
				self.category.add(category)
	
	class Meta:
		model = Product