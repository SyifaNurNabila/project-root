import json
from service.models import Product

def test_read_product(client):
    product = Product(name="ItemRead", category="ReadCat", price=12.34, available=True)
    product.create()
    response = client.get(f"/products/{product.id}")
    assert response.status_code == 200
    data = response.get_json()
    assert data["name"] == "ItemRead"

def test_update_product(client):
    product = Product(name="OldName", category="UpdateCat", price=11.11, available=True)
    product.create()
    new_data = {
        "name": "UpdatedName",
        "category": product.category,
        "price": product.price,
        "available": product.available
    }
    response = client.put(f"/products/{product.id}", json=new_data)
    assert response.status_code == 200
    updated = response.get_json()
    assert updated["name"] == "UpdatedName"

def test_delete_product(client):
    product = Product(name="ToDelete", category="DelCat", price=7.77, available=False)
    product.create()
    response = client.delete(f"/products/{product.id}")
    assert response.status_code == 204
    check = Product.find(product.id)
    assert check is None

def test_list_all_products(client):
    Product(name="A", category="CatA", price=1.11, available=True).create()
    Product(name="B", category="CatB", price=2.22, available=False).create()
    response = client.get("/products")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) >= 2

def test_list_by_name(client):
    name = "SpecialItem"
    Product(name=name, category="FilterCat", price=3.33, available=True).create()
    response = client.get(f"/products", query_string={"name": name})
    assert response.status_code == 200
    data = response.get_json()
    assert any(p["name"] == name for p in data)

def test_list_by_category(client):
    category = "Games"
    Product(name="Game1", category=category, price=4.44, available=True).create()
    response = client.get(f"/products", query_string={"category": category})
    assert response.status_code == 200
    data = response.get_json()
    assert all(p["category"] == category for p in data)

def test_list_by_availability(client):
    Product(name="AvailableItem", category="Office", price=5.55, available=True).create()
    response = client.get("/products", query_string={"available": "true"})
    assert response.status_code == 200
    data = response.get_json()
    assert all(p["available"] is True for p in data)
