import pytest

from product.models import Product


@pytest.mark.django_db
def test_create_product():
    product = Product.objects.create(
        title="Livro",
        description="Descrição do livro",
        price=50
    )

    assert product.title == "Livro"
    assert product.description == "Descrição do livro"
    assert product.price == 50
    assert product.id is not None