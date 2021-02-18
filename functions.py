import mysql.connector

def make_data(username):
    params = dict()
    (params['username'],params['heartfailpercent'],params['heartfailsevierity'])=databasefetcher(username)
    return params

def databasefetcher(username):
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="baka",
        database="healthcare"
    )
    cursor = db.cursor()
    sql = "SELECT * FROM outputtable WHERE username = %s"
    usr = (username, )

    cursor.execute(sql, usr)
    result = cursor.fetchall()
    return result[0]
