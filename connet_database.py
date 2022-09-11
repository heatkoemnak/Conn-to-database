import mysql.connector as connector

try:
    connection = connector.connect(host='localhost',
                                         database='hdsd',
                                         user='root',
                                         password='')

    mySql_insert_query = """INSERT INTO db (id,studentname,email, place) 
                           VALUES (%s,%s, %s, %s) """

    records_to_insert = [('1','HP Pavilion Power', 1999, '2019-01-11'),
                         ('2','MSI WS75 9TL-496', 5799, '2019-02-27'),
                         ('3','Microsoft Surface', 2330, '2019-07-23')]

    cursor = connection.cursor()
    cursor.executemany(mySql_insert_query, records_to_insert)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
