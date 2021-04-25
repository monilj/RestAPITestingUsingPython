import mysql.connector

# accepts 4 paramters host (where your mysql server is present),  database name , autheticatio username ,autheticatio password
conn = mysql.connector.connect(host='localhost', database='APIDevelop',
                               user='root', password='root')

print(conn.is_connected())
cursor_bj = conn.cursor()
cursor_bj.execute('select * from CustomerInfo')
row = cursor_bj.fetchone()
print(row)
print(row[3])
rowAll = cursor_bj.fetchall()
print(rowAll)
