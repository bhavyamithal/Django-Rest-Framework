import requests

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/?abc=123"

get_response = requests.post(endpoint, json={'title':'hello world!!', 'content':'None', 'price':123345})  # HTTP request

print(get_response.json()) # HTTP response status code

# print(get_response.json()['message']) # HTTP response status code
# print(get_response.status_code) # HTTP response status code
