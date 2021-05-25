# Import the required libraries
#import MySQLdb
import time
import pymysql
time.sleep(1)

# Site from reference: https://pynative.com/python-mysql-insert-data-into-database-table/
def dbConnection():
    try:
        connection = pymysql.connect(host='db', \
            user='root',\
            password='root',\
            db='')
        cursor = connection.cursor()
        cursor.execute("CREATE SCHEMA IF NOT EXISTS `challenge`")
        cursor.execute("CREATE TABLE IF NOT EXISTS challenge.correos(\
            `idCorreos` varchar(100) NOT NULL PRIMARY KEY, \
            `mailDate` date NOT NULL, \
            `Subject` varchar(200) NOT NULL, \
            `Sender` varchar(100) NOT NULL, \
            `Receiver` varchar(100) NOT NULL) COLLATE 'utf8mb4_bin'")
        cursor.execute("USE challenge")
        return connection, cursor
    except pymysql.Error as error:
        print("Failed to insert into MySQL table {}".format(error))


def newEntry(cursor, idCorreos, date, subject, sender, receiver):
    try:
        mySql_query = "INSERT INTO correos (`idCorreos`, `mailDate`, `Subject`, `Sender`, `Receiver`) VALUES (%s, %s, %s, %s, %s);"
        record = (idCorreos, date, subject, sender, receiver)
        cursor.execute(mySql_query, record)

    except pymysql.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

def checkIfExist(cursor):
    try:
        cursor.execute('SELECT idCorreos FROM challenge.correos')
        ids = cursor.fetchall()
        uniqueList = []
        for sublist in ids:
            for item in sublist:
                uniqueList.append(item)
        return uniqueList
    except pymysql.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

def dbSave(connection):
    connection.commit()
    connection.close()
