import mysql.connector as connector
try:
    conn=connector.connect(user='root',localhost='172.0.0.1',password='',batabase='hdsd')
    # cursor=connect.cursor()
    sql=INSERT INTO `db`(`studentname`, `email`, `place`) VALUES ('koemank','heatkoemnak@gmail.com','pursat')
    cursor = conn.cursor()
    conn.cursor(sql)
    conn.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()
except connector.error as err:
    print(err)
