import requests
from requests_oauthlib import OAuth2Session

# Set up authentication and create a session
client_id = "YOUR_APP_ID"
client_secret = "YOUR_APP_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
oauth = OAuth2Session(client_id, token={"access_token": access_token})

# Make a request to the Microsoft Graph API to get the user's tasks
response = oauth.get("https://graph.microsoft.com/beta/me/todo/lists/tasks")
tasks = response.json()["value"]

# Do something with the tasks
for task in tasks:
    print(task["title"])
