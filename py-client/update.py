import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "New title",
    # "content": "New content",
    "price": 1659.99
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())