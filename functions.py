import mysql.connector

def make_data(username):
    params = dict()
    (params['username'],params['heartfailpercent'],params['heartfailsevierity'])=databasefetcher(username)
    return params

def databasefetcher(username):
    db = mysql.connector.connect(
        host="remotemysql.com",
        user="hwW4R6cA0s",
        passwd="9bVe4xsxvX",
        db="hwW4R6cA0s"
    )
    cursor = db.cursor()
    sql = "SELECT * FROM healthcareai WHERE username = %s"
    usr = (username, )
    cursor.execute(sql, usr)
    result = cursor.fetchall()
    return result[0]
