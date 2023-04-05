import requests

endpoint = 'http://127.0.0.1:8000/api/'

get_response = requests.post(endpoint, json={'title': 'New Title', 'description': 'New Description', 'price': 19.99})
print(get_response.json())