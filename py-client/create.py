import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "New Product",
    "price": 100.00,
    "description": "New Product Description",
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())