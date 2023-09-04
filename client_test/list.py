import requests
import getpass

# Username and password for authentication
username = input("Enter Username: ")
password = getpass.getpass("Enter Password: ")

# Authentication endpoint
auth_endpoint = "http://localhost:8000/api/auth/"

# Make a POST request to authenticate
auth_response = requests.post(
    auth_endpoint, json={"username": username, "password": password}
)

if auth_response.status_code == 200:
    # Get the token from the response
    token = auth_response.json()["token"]
    # Create the headers for authentication
    headers = {"Authorization": f"Token {token}"}
    # Endpoint for listing users
    endpoint = "http://localhost:8000/user/users/"
    # Make a GET request to list users
    get_response = requests.get(endpoint, headers=headers)
    # Get the JSON response
    json_response = get_response.json()

    print(json_response)
else:
    print("Authentication failed. Status code:", auth_response.status_code)