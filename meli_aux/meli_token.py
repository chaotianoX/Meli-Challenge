# Import the required libraries
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Source: https://developers.google.com/gmail/api/quickstart/python
# This function get the user's credentials. 
def getCredentials():
    creds = None  
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        print('Run "python3 start.py" to validate Gmail credentials')
    
    return build('gmail', 'v1', credentials=creds)
