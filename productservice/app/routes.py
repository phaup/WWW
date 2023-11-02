from flask import Blueprint, request, jsonify
from .models import Product

product_blueprint = Blueprint('product_blueprint', __name__)

@product_blueprint.route('/product', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(id=data['id'], name=data['name'], price=data['price'], description=data['description'])
    Product.add_product(product)
    return jsonify(product.__dict__), 201

@product_blueprint.route('/product/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.find_by_id(id)
    return jsonify(product.__dict__) if product else ('', 404)

@product_blueprint.route('/product/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.find_by_id(id)
    if product:
        Product.remove_product(product)
        return '', 204
    return '', 404
