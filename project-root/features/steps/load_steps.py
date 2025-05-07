from behave import given
import requests

@given('the following products')
def step_impl(context):
    """Load the product data into the database"""
    headers = {"Content-Type": "application/json"}
    for row in context.table:
        payload = {
            "name": row['name'],
            "category": row['category'],
            "price": float(row['price']),
            "available": row['available'].lower() == "true"
        }
        response = requests.post("http://localhost:5000/products", json=payload, headers=headers)
        assert response.status_code == 201
