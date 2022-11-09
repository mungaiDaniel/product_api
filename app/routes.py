from app import app, db, ma
from app.model import Product, product_schema, products_schema
from flask import request, jsonify, make_response

@app.route('/product', methods=['POST'])
def add_product():
    data = request.get_json()
    name = data['name']
    description = data['description']
    price = data['price']
    qty = data['qty']
    podct = Product(name=name, description=description, price=price, qty=qty)

    db.session.add(podct)
    db.session.commit()

    return product_schema.jsonify(podct)

@app.route('/product', methods=['GET'])
def get_all():
    product = Product.query.all()
    result = products_schema.dump(product)

    return make_response(jsonify({
        "status": 200,
        "data": result
    }), 200)

@app.route('/product/<int:id>', methods=['GET'])
def get_one(id):
    product = Product.query.get_or_404(id)

    return product_schema.dump(product), 200

@app.route('/product/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    name = data['name']
    description = data['description']
    price = data['price']
    qty = data['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty
    
    db.session.commit()

    return product_schema.jsonify(product), 200

@app.route('/product/<int:id>', methods=['DELETE'])
def delete(id):
    product = Product.query.get_or_404(id)

    if not product:
        return jsonify({'message': 'No user found'}), 401

    

    db.session.delete(product)
    db.session.commit()
    
    return jsonify({"message": "deleted sucessfully"}), 200