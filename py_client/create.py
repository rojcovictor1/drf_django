import requests


headers = {'Authorization': 'Bearer e156b56ad167b4e671d03d6990fad941924b28a4'}
endpoint = 'http://localhost:8000/api/products/'


data = {
    'title': 'This field is done',
    'price': 32.99
}

get_response = requests.post(endpoint, json=data, headers=headers)


print(get_response.json())
