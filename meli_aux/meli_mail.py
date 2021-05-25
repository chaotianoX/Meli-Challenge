# Import the required libraries
import dateutil.parser as parser
from apiclient import errors
from . import meli_token as cred

# Connect to the Gmail API 
service = cred.getCredentials()

# Documentation used: https://developers.google.com/gmail/api/reference/rest
# This function search for a especific word and return all the mails that compliance with that. 
def getEmails():
    try:
        palabra = 'DevOps' # You can change DevOps for any word
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

# This function will extract the information needed from the specific message
#   and return the values that want to be stored in the database
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
                   