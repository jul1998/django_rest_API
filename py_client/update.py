import requests

endpoint = 'http://127.0.0.1:8000/api/products/1/edit'

data = {
    'title': 'New Title',
    'price': 19.99,
    'description': 'New Description'
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())