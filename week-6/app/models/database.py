import mysql.connector
from mysql.connector import errorcode

cnx = None

def get_connection(config):
    global cnx
    if not cnx:
        try:
            cnx = mysql.connector.connect(**config)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            else:
                print(err)
        return cnx
    else:
        return cnx

def get_cursor(config):
    cnx = get_connection(config)
    cnx.reconnect()
    cursor = cnx.cursor(dictionary=True)
    return (cnx, cursor)
