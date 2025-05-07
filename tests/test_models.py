from service.models import Product

def test_read_product():
    product = Product(name="Test", category="Book", price=10.99, available=True)
    product.create()
    found = Product.find(product.id)
    assert found is not None
    assert found.id == product.id

def test_update_product():
    product = Product(name="Old", category="Book", price=5.00, available=True)
    product.create()
    product.name = "New"
    product.update()
    updated = Product.find(product.id)
    assert updated.name == "New"

def test_delete_product():
    product = Product(name="ToDelete", category="Book", price=9.99, available=True)
    product.create()
    product_id = product.id
    product.delete()
    result = Product.find(product_id)
    assert result is None

def test_list_all_products():
    Product(name="One", category="Book", price=1.00, available=True).create()
    Product(name="Two", category="Game", price=2.00, available=False).create()
    all_products = Product.all()
    assert len(all_products) >= 2

def test_find_by_name():
    Product(name="UniqueName", category="Book", price=3.00, available=True).create()
    results = Product.find_by_name("UniqueName")
    assert any(p.name == "UniqueName" for p in results)

def test_find_by_category():
    Product(name="GameItem", category="Games", price=4.50, available=True).create()
    results = Product.find_by_category("Games")
    assert any(p.category == "Games" for p in results)

def test_find_by_availability():
    Product(name="InStock", category="Office", price=6.00, available=True).create()
    results = Product.find_by_availability(True)
    assert all(p.available is True for p in results)
