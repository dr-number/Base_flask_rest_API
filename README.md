# Base flask REST API

## How to build

Build

    docker-compose build

## How to start

And run composition

    docker-compose up -d

## How to use

HTTP Headers
- Set http headers **content-type** to **application/json**

### Get all products
Method **GET**

http://127.0.0.1:5000/products/

**Body JSON content**
```json
{
  "name": "Product_1",
  "description": "Product number one",
  "price": 100.00,
  "qty": 3
}
```

**Example response** (return product id)
```json
{
  "id": 1
}
```

### Get product by id
Method **GET**

http://127.0.0.1:5000/product/<product_id>

**Example response**
```json
{
  "description": "Product number one",
  "id": 1,
  "name": "Product_1",
  "price": 100.0,
  "qty": 3
}
```