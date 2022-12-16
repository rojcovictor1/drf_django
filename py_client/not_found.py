import requests


endpoint = 'http://localhost:8000/api/products/1215345646686456465/'

get_response = requests.get(endpoint)


print(get_response.json())
