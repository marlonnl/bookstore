import pytest

from order.models import Order
from order.factories import OrderFactory, ProductFactory


@pytest.mark.django_db
def test_create_order():
	product1 = ProductFactory()
	product2 = ProductFactory()

	order = OrderFactory(product=(product1, product2))

	print("produt1", product1)
	print("produt2", product2)
	print("order", order.product)


	# assert order.product[0]["title"] == product1.title

	# def test_create_product():
    # product = Product.objects.create(
    #     title="Livro",
    #     description="Descrição do livro",
    #     price=50
    # )

    # assert product.title == "Livro"
    # assert product.description == "Descrição do livro"
    # assert product.price == 50
    # assert product.id is not None