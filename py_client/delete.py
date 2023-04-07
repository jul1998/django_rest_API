import requests



product_id = int(2)
endpoint = f'http://127.0.0.1:8000/api/products/{product_id}/delete'
try:
    response = requests.delete(endpoint)
    response.raise_for_status()  # raises an exception if the response has a status code indicating a failure
    print(response.status_code)
except requests.exceptions.RequestException as e:
    print("Error: ", e)