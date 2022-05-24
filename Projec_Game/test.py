import mysql.connector
mydb1 = mysql.connector.connect(
    port=3306,
    user="root",
    password="12345",
  database="game_db"
  )
mycursor = mydb1.cursor()

query_table='''CREATE TABLE user_details (
    email_id varchar(20) PRIMARY KEY,
    username VARCHAR(20),
    phone_number varchar(20),
    date_of_birth varchar(20))'''
mycursor.execute(query_table)
