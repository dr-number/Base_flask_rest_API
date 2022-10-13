from database import db
from config import Config

from flask import Flask, jsonify, request
from models.Product import Product, ProductSchema


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = Config.BASE_PATH
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


@app.route("/", methods=["get"])
def start():
    db.create_all()
    return jsonify({ 'status': 'API working...' })


@app.route('/product/all', methods=['GET'])
def get_all_products():
    try:
        result = products_schema.dump(Product.query.all())
        return jsonify({
            "count": len(result),
            "products": result
        })
    except Exception as e:
        return jsonify({ 'error': e.args[0] })


@app.route('/product/', methods=['POST'])
def create_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)

    try:    
        db.session.add(new_product)
        db.session.commit()
        return product_schema.jsonify({ 'id': new_product.id })
    except Exception as e:
        return jsonify({ 'error': e.args[0] })

@app.route('/product/<id>', methods=['PUT'])
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
        return jsonify({ 'status': 'ok' })
    except Exception as e:
        return jsonify({ 'error': e.args[0] })


@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    try:
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()
        return jsonify({ 'status': 'ok' })
    except Exception as e:
        return jsonify({ 'error': e.args[0] })

@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    try:
        p = Product.query.get(id)
        product = product_schema.dump(p)
        return jsonify(product)
    except Exception as e:
        return jsonify({ 'error': e.args[0] })

if __name__ == '__main__':
    app.run(port=5000)


