
def insert_data(email_id,username,phone_number,date_of_birth,Score=0):
    import mysql.connector
    mydb1 = mysql.connector.connect(
        port=3306,
        user="root",
        password="12345",
        database="game_db1"
    )
    mycursor = mydb1.cursor()
    sql = "INSERT INTO user_details VALUES (%s,%s,%s,%s,%s)"
    val = (email_id,username,phone_number,date_of_birth,Score)
    mycursor.execute(sql, val)
    mydb1.commit()
    mydb1.close()
    return True