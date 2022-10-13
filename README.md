# Base flask REST API (with sqlite)

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
http://127.0.0.1:5000/products/

Method **GET**

**Body JSON content**
```json
{
  "name": "Product_1",
  "description": "Product number one",
  "price": 100.00,
  "qty": 3
}
```

**Example response**
```json
{
  "count": 1,
  "products": [
    {
      "description": "Product number one",
      "id": 1,
      "name": "Product_1",
      "price": 100.0,
      "qty": 3
    }
  ]
}
```

### Get product by id
http://127.0.0.1:5000/product/<product_id>

Method **GET**

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

### Create product
http://127.0.0.1:5000/product/

Method **POST**

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

### Update product
http://127.0.0.1:5000/product/<product_id>

Method **PUT**

**Example Body JSON content**
```json
{
  "price": 100.00,
  "qty": 3
}
```

**Example response**
```json
{ 
    "status": "ok"
}
```