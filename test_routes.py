import unittest
from app import app  # Assuming 'app' is your Flask app or FastAPI app

class TestProductRoutes(unittest.TestCase):
    # 3a: READ (Get Product by ID)
    def test_read_product(self):
        response = app.test_client().get('/products/1')  # Adjust your endpoint as needed
        self.assertEqual(response.status_code, 200)
        self.assertIn('Product Name', response.data.decode())

    # 3b: UPDATE (Update Product)
    def test_update_product(self):
        data = {'name': 'Updated Product', 'price': 20}
        response = app.test_client().put('/products/1', json=data)  # Adjust your endpoint as needed
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated Product', response.data.decode())

    # 3c: DELETE (Delete Product)
    def test_delete_product(self):
        response = app.test_client().delete('/products/1')  # Adjust your endpoint as needed
        self.assertEqual(response.status_code, 200)
        # You can also test that the product no longer exists by trying to get it after deletion
        response = app.test_client().get('/products/1')
        self.assertEqual(response.status_code, 404)

    # 3d: LIST ALL (List all Products)
    def test_list_all_products(self):
        response = app.test_client().get('/products')  # Adjust your endpoint as needed
        self.assertEqual(response.status_code, 200)
        self.assertIn('Product Name', response.data.decode())

    # 3e: LIST BY NAME (Filter Products by Name)
    def test_list_by_name(self):
        response = app.test_client().get('/products?name=Product Name')  # Adjust your endpoint as needed
        self.assertEqual(response.status_code, 200)
        self.assertIn('Product Name', response.data.decode())

    # 3f: LIST BY CATEGORY (Filter Products by Category)
    def test_list_by_category(self):
        response = app.test_client().get('/products?category=Category')  # Adjust your endpoint as needed
        self.assertEqual(response.status_code, 200)
        self.assertIn('Category', response.data.decode())

    # 3g: LIST BY AVAILABILITY (Filter Products by Availability)
    def test_list_by_availability(self):
        response = app.test_client().get('/products?availability=true')  # Adjust your endpoint as needed
        self.assertEqual(response.status_code, 200)
        self.assertIn('Available', response.data.decode())
