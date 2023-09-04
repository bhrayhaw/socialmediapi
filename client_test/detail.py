import requests

endpoint = 'http://localhost:8000/api/user_registration/1'

get_response = requests.get(endpoint)

print(get_response.json())