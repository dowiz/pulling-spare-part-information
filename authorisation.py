import requests
from bs4 import BeautifulSoup


# Create a session
session = requests.Session()


# Parse the login page HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract the CSRF token from the login form
access_token = soup.find("input", {"name": "client_secret"})["value"]

# Prepare the login data
login_data = {
    "access_token": access_token,
    "username": username,
    "password": password
}

# Send a POST request to the login endpoint
login_url = "https://www.repxpert.ua/uk/login"
response = session.post(login_url, data=login_data)

# Check if the login was successful
if response.status_code == 200:
    print("Login successful!")
    # Continue with the rest of your code here
else:
    print("Login failed!")
    # Handle the login failure case here
