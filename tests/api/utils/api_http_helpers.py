import requests

from config import API_BASE_URL
from tests.api.data_models import AuthenticationError, CreateUserError, GetUserError, UpdateUserError

def authenticate(username, password):
    authUrl =  f"{API_BASE_URL}/Provider/Login"
    credentials = {
        "UserName": username,
        "Password": password
    }
    response = requests.post(authUrl, json=credentials)
    if response.status_code != 200:
            raise AuthenticationError(f"Authentication failed with status code {response.status_code}")
    token = response.json().get("access_token")
    if token is None:
            raise AuthenticationError(f"Authentication endpoint returned no token.")
    return token

def get_user_by_id(api_credentials, user_id):
    url = f"{API_BASE_URL}/Users/{user_id}"
    headers = {"Authorization": f"Bearer {api_credentials.auth_token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
            raise GetUserError(f"Get user endpoint failed with status code {response.status_code}")
    # for some reason, endpoint responds with status code 200 and empty response, when non existing userId provided
    get_user_details = response.json()
    if not get_user_details:
          raise GetUserError(f'Get user endpoint returned empty user details')
    return response.json()

def create_user(api_credentials, user_details):
    url_create_user = f"{API_BASE_URL}/Users"
    user_data = {"Email": user_details.email, "Enabled": True, "Password": user_details.password, "FirstName" : user_details.first_name, "LastName" : user_details.last_name}
    headers = {"Authorization": f"Bearer {api_credentials.auth_token}"}
    response = requests.post(url_create_user, json=user_data, headers=headers)
    if response.status_code != 200:
        raise CreateUserError(f"Create user endpoint failed with status code: {response.status_code}")
    user_id = response.json()

    # Create user end point returns status 200 even if it has failed to create a new user.
    # In such cases, it returns error message instead of new user id inside of http response.
    # So, we manually check for known error messages here.
    if user_id in ("Email already exist.", "No token received"):
        raise CreateUserError(f"Create user endpoint failed with response message: {user_id}.")
    return user_id

def update_user(api_credentials, user_details):
    url_update_user = f"{API_BASE_URL}/Users"
    user_data = {"ID" : user_details.id, "Email": user_details.email, "Enabled": True, "Password": user_details.password, "FirstName" : user_details.first_name, "LastName" : user_details.last_name}
    headers = {"Authorization": f"Bearer {api_credentials.auth_token}"}
    response = requests.put(url_update_user, json=user_data, headers=headers)
    if response.status_code != 200:
        raise UpdateUserError(f"Update user endpoint failed with status code: {response.status_code}")

def delete_user(api_credentials, user_id):
    url_delete_user = f"{API_BASE_URL}/Users/{user_id}"
    headers = {"Authorization": f"Bearer {api_credentials.auth_token}"}
    response = requests.delete(url_delete_user, headers=headers)
    if response.status_code != 200:
            raise GetUserError(f"Delete user endpoint failed with status code {response.status_code}")
