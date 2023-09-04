import requests

user_id = int(input('Which user do you want to remove: '))

try: 
    user_id
except:
    user_id = None
    print("Please enter a valid user")

if user_id:
    endpoint = f"http://localhost:8000/api/user_registration/{user_id}/update"
    get_response = requests.put(endpoint, json={'first_name': 'Jones', 'last_name': 'Appiah', 'email': 'appiah@appiah.com', 'password': '1234'})
    print(get_response.json())
