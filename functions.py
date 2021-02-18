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
    val = (username, )
    cursor.execute(sql, val)
    result = cursor.fetchall()
    return result[0]

def databaseentry(username,anemia,diabetes,bloodpressure,gender):
    db = mysql.connector.connect(
        host="remotemysql.com",
        user="hwW4R6cA0s",
        passwd="9bVe4xsxvX",
        db="hwW4R6cA0s"
    )
    cursor = db.cursor()
    sql = "INSERT INTO healthcareaiinput VALUES (%s,%s,%s,%s,%s)"
    val = (username,anemia,diabetes,bloodpressure,gender)
    try:
        cursor.execute(sql, val)
        db.commit()
        return "successful"
    except:
        return "unsuccessful"
