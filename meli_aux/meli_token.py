# Import the required libraries
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# This function get the user's credentials. Source: https://developers.google.com/gmail/api/quickstart/python
def getCredentials():
    creds = None  
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time
    if os.path.exists('./cred/token.json'):
        creds = Credentials.from_authorized_user_file('./cred/token.json', SCOPES)  
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('./cred/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        # Save the credentials for the next run
        with open('./cred/token.json', 'w') as token:
            token.write(creds.to_json())
    
    # Return a object with the credentials that can be used by any other module
    return build('gmail', 'v1', credentials=creds)
