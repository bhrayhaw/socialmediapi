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
    # Endpoint for creating a user
    endpoint = "http://localhost:8000/user/register/"
    # Make a POST request to create a user
    get_response = requests.post(
        endpoint,
        json={
            "first_name": "nanaba",
            "username": "nana",
            "last_name": "Appiah",
            "email": "na@appiah.com",
            "password": "1234",
        },
        headers=headers,
    )
    # Get the JSON response
    json_response = get_response.json()

    print(json_response)
else:
    print("Authentication failed. Status code:", auth_response.status_code)
