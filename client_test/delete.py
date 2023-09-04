import requests

user_id = int(input('Which user do you want to remove: '))

try:
    user_id
except:
    user_id = None
    print("Please enter a valid user")

if user_id:
    endpoint = f"http://localhost:8000/api/user_registration/{user_id}/delete"
    get_response = requests.delete(endpoint)
    print(get_response.json())
