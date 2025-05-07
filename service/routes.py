from flask import Blueprint, jsonify, request, abort
from service.models import Product

bp = Blueprint("products", __name__, url_prefix="/products")

@bp.route("/<int:product_id>", methods=["GET"])
def read_product(product_id):
    product = Product.find(product_id)
    if not product:
        abort(404, description="Product not found")
    return jsonify(product.serialize()), 200

@bp.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.find(product_id)
    if not product:
        abort(404, description="Product not found")

    data = request.get_json()
    product.name = data.get("name", product.name)
    product.category = data.get("category", product.category)
    product.price = data.get("price", product.price)
    product.available = data.get("available", product.available)
    product.update()

    return jsonify(product.serialize()), 200

@bp.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.find(product_id)
    if not product:
        abort(404, description="Product not found")
    product.delete()
    return "", 204

@bp.route("", methods=["GET"])
def list_products():
    name = request.args.get("name")
    category = request.args.get("category")
    available = request.args.get("available")

    if name:
        products = Product.find_by_name(name)
    elif category:
        products = Product.find_by_category(category)
    elif available:
        is_available = available.lower() == "true"
        products = Product.find_by_availability(is_available)
    else:
        products = Product.all()

    return jsonify([p.serialize() for p in products]), 200
