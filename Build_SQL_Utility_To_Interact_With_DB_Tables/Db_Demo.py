import mysql.connector
from util.configurations import *
# accepts 4 paramters host (where your mysql server is present),  database name , autheticatio username ,autheticatio password
# conn = mysql.connector.connect(host='localhost', database='APIDevelop',
#                                user='root', password='root')
conn = getConnection()
print(conn.is_connected())
cursor_bj = conn.cursor()
cursor_bj.execute('select * from CustomerInfo')
# row = cursor_bj.fetchone()
# print(row)
# print(row[3])
# rowAll = cursor_bj.fetchall()
# print(rowAll)

rows = cursor_bj.fetchall()
print(rows)

sum = 0
for row in rows:
    sum = sum + row[2]
print(sum)

query = "update customerInfo set Location = %s where CourseName = %s"
data = ("UK", "Jmeter")
cursor_bj.execute(query, data)
conn.commit()
delete_query = "delete from customerInfo where courseName = %s"
data2 = ("WebServices",)
cursor_bj.execute(delete_query,data2)
conn.commit()
conn.close()
