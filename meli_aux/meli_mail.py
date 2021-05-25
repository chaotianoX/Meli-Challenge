# Import the required libraries
import dateutil.parser as parser
from apiclient import errors
from . import meli_token as cred

# Connect to the Gmail API
service = cred.getCredentials()

# This function search for the mails that. Link used: https://developers.google.com/gmail/api/reference/rest
def getEmails():
    try:
        palabra = "DevOps"
        # Call the Gmail API
        result = service.users().messages().list(userId='me', q=palabra).execute()
        mails = []

        if 'messages' in result:
            mails.extend(result['messages'])
        
        while 'nextPageToken' in result:
            page_token = result['nextPageToken']
            result = service.users().messages().list(userId='me', q=palabra, pageToken=page_token).execute()
            mails.extend(result['messages'])
        
        return mails
    except errors.HttpError as error:
        print('An error occurred: %s' %error)

# This function would extract the information needed from the specific message object
def extractInfo(msg_id):
    try:
        message = service.users().messages().get(userId='me', id=msg_id, format='metadata').execute()
        headers = message['payload']['headers']
        subject = '-- NO SUBJECT --'
        for header in headers:
            if header['name'] == 'Date':
                text_date = header['value']
                parsing = (parser.parse(text_date))
                date = (parsing.date())
            if header['name'] == 'Subject':
                if header['value'] == '':
                    pass
                else:
                    subject = header['value']
            if header['name'] == 'From':
                sender = header['value']
            if header['name'] == 'To':
                receiver = header['value']
        return(date, subject, sender, receiver)
    except errors.HttpError as error:
        print ('Error al recuperar un mensaje: %s' % error)
                   