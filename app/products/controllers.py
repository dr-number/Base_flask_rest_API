import json
from ..database import db
from flask import jsonify, request, Blueprint
from .models import Product, ProductSchema

__STATUS_GOOD = { 'status': 'ok' }
__STATUS_NOT_FOUND = { 'status': 'not found' }

module = Blueprint('products', __name__)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

def __get_error(e: Exception) -> str:
    return jsonify({ 'error': e.args[0] })


def __get_msg_initial_error(key: str = '') -> str:
    if not key:
        return jsonify({ 'error': f'Initial data not entered!' })

    return jsonify({ 'error': f'Initial data \'{key}\' not entered!' })


def __is_all_initial_data(request: request, keys: list) -> str:

    if not request.content_type or request.content_type.lower() != 'application/json':
        return jsonify({ 'error': 'Content type should be application/json!' })

    data_json = None

    try:
        data_json = json.loads(request.data)
    except Exception as e:
        return jsonify({ 'error': 'Not valid json in header!' })

    if not data_json:
        return __get_msg_initial_error()

    for key in keys:
        if not key in data_json:
            return __get_msg_initial_error(key)

    return ''


@module.route('/products/', methods=['GET'])
def get_all_products():
    try:
        result = products_schema.dump(Product.query.all())
        return jsonify({
            "count": len(result),
            "products": result
        })
    except Exception as e:
        return __get_error(e)


@module.route('/product/<id>', methods=['GET'])
def get_product(id):
    try:
        product = Product.query.get(id)
        
        if not product:
            return jsonify(__STATUS_NOT_FOUND)

        return jsonify(product_schema.dump(product))
    except Exception as e:
        return __get_error(e)


@module.route('/product/', methods=['POST'])
def create_product():

    is_error = __is_all_initial_data(request, ['name', 'description', 'price', 'qty'])

    if is_error:
        return is_error

    data = request.json
    new_product = Product(data['name'], data['description'], data['price'], data['qty'])

    try:
        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify({ 'id': new_product.id })
    except Exception as e:
        return __get_error(e)


@module.route('/product/<id>', methods=['PUT'])
def update_product(id):
    data = request.json

    try:
        product = Product.query.get(id)

        if 'name' in data:
            product.name = data['name']

        if 'description' in data:
            product.description = data['description']

        if 'price' in data:
            product.price = data['price']

        if 'qty' in data:
            product.qty = data['qty']
    
        db.session.commit()
        return jsonify(__STATUS_GOOD)
    except Exception as e:
        return __get_error(e)


@module.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    try:
        product = Product.query.get(id)

        if not product:
            return jsonify(__STATUS_NOT_FOUND)

        db.session.delete(product)
        db.session.commit()
        return jsonify(__STATUS_GOOD)
    except Exception as e:
        return __get_error(e)
