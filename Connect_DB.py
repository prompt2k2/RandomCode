import mysql.connector


conn = mysql.connector.connect(user='eagle_eye_master@eagle-eye-db', password='Pa33w0rd',
                               host='eagle-eye-db.mysql.database.azure.com', database='eagle_eye')

conn.close()
