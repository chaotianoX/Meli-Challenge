# Import the required libraries
from meli_aux import meli_db as DB
from meli_aux import meli_mail as mail

def main():
    messages = mail.getEmails()
    conn, cursor = DB.dbConnection()
    id_list = DB.checkIfExist(cursor)
    inserts = 0
    for message in messages:
        if message['id'] not in id_list:
            date, subject, sender, receiver = mail.extractInfo(message['id'])
            DB.newEntry(cursor, message['id'], date, subject, sender, receiver)
            inserts += 1
    if inserts > 0:
        DB.dbSave(conn)
        print(str(inserts)+' new entries were registered in database')
    else:
        print('There were no new entries')       

if __name__ == '__main__':
    main()