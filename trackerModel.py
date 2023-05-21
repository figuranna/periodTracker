import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="periodtracker",
    auth_plugin="mysql_native_password" #caching sha2 password
)

mycursor = db.cursor()
lastId = mycursor.lastrowid
dates = []
tmpDates = []

def insertPeriod(data):
    q1 = "INSERT INTO period (datePeriod) VALUES (%s)"
    mycursor.execute(q1, (data,))
    lastId = mycursor.lastrowid
    db.commit()

def insertSymptoms(data1,data2,data3):
    q2 = "INSERT INTO symptoms (symptomId, flow, mood, bodySymptoms) VALUES (%s,%s,%s,%s)"
    mycursor.execute(q2, (lastId,data1,data2,data3))
    db.commit()

def selectFiveDates():
    mycursor.execute("SELECT datePeriod FROM period ORDER BY periodId DESC LIMIT 5")
    for x in mycursor:
        dates.append(x)
    return dates
