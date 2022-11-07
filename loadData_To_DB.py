"""
Read Data from CSV file and load the data into database(MySQL DB)
"""

import csv
import pandas as pd
import MySQLdb

filepath = "./Data/Employee.csv"
mydb = MySQLdb.connect(host='127.0.0.1',user='root',passwd='root',db='Employee')
cursor = mydb.cursor()

df = pd.read_csv(filepath)


cursor.execute("DELETE FROM EmployeeInfo")

sql = 'INSERT INTO EmployeeInfo(Experience_Years,Age,Gender, Salary) VALUES(%s, %s, %s , %s)'
for row in df.itertuples():
    val = (row[2],row[3],row[4],row[5])
    cursor.execute(sql, val)

mydb.commit()
cursor.close()
    