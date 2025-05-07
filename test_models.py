import unittest
from models import Product  # Assuming Product model exists

class TestProductModel(unittest.TestCase):
    # 2a: READ
    def test_read_product(self):
        product = Product.query.get(1)
        self.assertIsNotNone(product)

    # 2b: UPDATE
    def test_update_product(self):
        product = Product.query.get(1)
        product.name = "Updated Product"
        product.save()
        self.assertEqual(product.name, "Updated Product")

    # 2c: DELETE
    def test_delete_product(self):
        product = Product.query.get(1)
        product.delete()
        self.assertIsNone(Product.query.get(1))

    # 2d: LIST ALL
    def test_list_all_products(self):
        products = Product.query.all()
        self.assertGreater(len(products), 0)

    # 2e: FIND BY NAME
    def test_find_by_name(self):
        product = Product.query.filter_by(name="Product Name").first()
        self.assertEqual(product.name, "Product Name")

    # 2f: FIND BY CATEGORY
    def test_find_by_category(self):
        products = Product.query.filter_by(category="Category").all()
        self.assertGreater(len(products), 0)

    # 2g: FIND BY AVAILABILITY
    def test_find_by_availability(self):
        products = Product.query.filter_by(availability=True).all()
        self.assertGreater(len(products), 0)
