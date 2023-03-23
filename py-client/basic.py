import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/?abc=123"

get_response = requests.get(endpoint, params={"abc": 123}, json={'query':'hello world!!'})  # HTTP request

print(get_response.json()) # HTTP response status code

# print(get_response.json()['message']) # HTTP response status code
# print(get_response.status_code) # HTTP response status code
