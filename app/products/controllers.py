from ..database import db
from flask import jsonify, request, Blueprint
from .models import Product, ProductSchema
from werkzeug.exceptions import BadRequest

__STATUS_GOOD = { 'status': 'ok' }
__STATUS_NOT_FOUND = { 'status': 'not found' }
__ERROR_HEADER_JSON = { 'error': 'Not valid json in header!' }
__ERROR_MAYBE_HEADER_JSON = { 'error': 'Bad request! Maybe not valid json in header!' }

module = Blueprint('products', __name__)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

def __get_error(e: Exception) -> str:
    return jsonify({ 'error': e.args[0] })

def __get_error_bad_request(e: Exception) -> str:
    return jsonify(__ERROR_MAYBE_HEADER_JSON)

def __get_msg_initial_error(e: Exception) -> str:
    return jsonify({ 'error': 'Initial data: \'' + e.args[0] + '\' not entered!' })


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

    try:
        data = request.json
        new_product = Product(data['name'], data['description'], data['price'], data['qty'])

        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify({ 'id': new_product.id })

    except ValueError as e:
        return jsonify(__ERROR_HEADER_JSON)
    except KeyError as e:
        return __get_msg_initial_error(e)
    except BadRequest as e:
        return __get_error_bad_request(e)
    except Exception as e:
        return __get_error(e)


@module.route('/product/<id>', methods=['PUT'])
def update_product(id):

    try:
        data = request.json
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
        
    except ValueError as e:
        return jsonify(__ERROR_HEADER_JSON)
    except KeyError as e:
        return __get_msg_initial_error(e)
    except BadRequest as e:
        return __get_error_bad_request(e)
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
