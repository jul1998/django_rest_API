import requests

endpoint = 'http://127.0.0.1:8000/api/products/'

post_data = {
    'title': 'New Product',
    'description': 'New Product Description',
    'price': 19.99
}

get_response = requests.post(endpoint,post_data)
print(get_response.json())