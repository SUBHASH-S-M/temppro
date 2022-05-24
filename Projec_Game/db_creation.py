import mysql.connector
mydb = mysql.connector.connect(
  port=3306,
  user="root",
  password="12345"
)
mycursor = mydb.cursor()
db_name="game_db1"
try:
  mycursor.execute(f"CREATE DATABASE {db_name}")
except:
  print("DB alrady exisits")
finally:
  print("DB ok")
  mydb.close()
try:
  import mysql.connector

  mydb1 = mysql.connector.connect(
    port=3306,
    user="root",
    password="12345",
    database="game_db1"
  )
  mycursor = mydb1.cursor()

  query_table = '''CREATE TABLE user_details (
      email_id varchar(50) PRIMARY KEY,
      username VARCHAR(20),
      phone_number varchar(20),
      date_of_birth varchar(20),Score int DEFAULT 0)'''
  mycursor.execute(query_table)

except :
  print("Table exists already ")
finally:
  print("Table ok")
  mydb1.close()

