# Base flask REST API

## How to build

Build

    docker-compose build

## How to start

And run composition

    docker-compose up -d

## How to use

**Get all products**
Method **GET**

http://127.0.0.1:5000/products/

**JSON content**
{
  "name": "Product_1",
  "description": "Product number one",
  "price": 100.00,
  "qty": 3
}
