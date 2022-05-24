from random import *
from turtle import *
from freegames import vector

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os
from db_operations import *
def insert_score(Score):
    import mysql.connector
    mydb1 = mysql.connector.connect(
        port=3306,
        user="root",
        password="12345",
        database="game_db1"
    )
    mycursor = mydb1.cursor()
    sql = f"UPDATE user_details set score={Score}"
    mycursor.execute(sql)
    mydb1.commit()
def main_game():

    bird = vector(0, 0)
    balls = []

    # Start Time Of the Game

    from datetime import datetime

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")


    def tap(x, y):
        """Move bird up in response to screen tap."""
        up = vector(0, 30)
        bird.move(up)


    def inside(point):
        """Return True if point on screen."""
        return -200 < point.x < 200 and -200 < point.y < 200


    def draw(alive):
        """Draw screen objects."""
        clear()

        goto(bird.x, bird.y)

        if alive:
            dot(10, 'green')
        else:
            dot(10, 'red')
            new = datetime.now()
            end_time = new.strftime("%H:%M:%S")

            FMT = '%H:%M:%S'
            tdelta = datetime.strptime(end_time, FMT) - datetime.strptime(current_time, FMT)
            total_sec = tdelta.seconds

            Score = total_sec * 3
            insert_score(Score)

        for ball in balls:
            goto(ball.x, ball.y)
            dot(20, 'black')

        update()


    def move():
        """Update object positions."""
        bird.y -= 5

        for ball in balls:
            ball.x -= 3

        if randrange(10) == 0:
            y = randrange(-199, 199)
            ball = vector(199, y)
            balls.append(ball)

        while len(balls) > 0 and not inside(balls[0]):
            balls.pop(0)

        if not inside(bird):
            draw(False)
            return

        for ball in balls:
            if abs(ball - bird) < 15:
                draw(False)
                return

        draw(True)
        ontimer(move, 50)


    setup(420, 420, 370, 0)
    hideturtle()
    up()
    tracer(False)
    onscreenclick(tap)
    move()
    done()







def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


import re

def check(email,dob,phone):
    regexe = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    regexp="[0-9]"
    regexd="[\d]{1,2}-[\d]{1,2}-[\d]{4}"
    d={"email":[],"dob":[],'phone':[]}
    print(re.search(regexe,email))
    if (re.search(regexe,email)):
        d['email']=[True,"Valid Email"]
    else:
        d['email']=[False,"InValid Email"]
    if (re.search(regexp,phone)):
        d['phone']=[True,"Valid phone"]
    else:
        d['phone']=[False,"InValid phone"]
    if (re.search(regexd, dob)):
        d['dob'] = [True, "Valid dob"]
        dob_for=dob[3:5]
        dob_da=dob[0:2]
        flag=True
        if(dob_for[0]!='0' or dob_da[0]!='0' ):
            if(int(dob_for)>12 or int(dob_da)>31):
                flag=False
        if(flag):
            d['dob']=[flag,"Valid DOB"]
    else:
        d['dob'] = [False, "InValid dob"]
    print(d)
    return d

def main():
    local_css("style.css")
    activities = [ "Registration","ABOUT"]
    choice = st.sidebar.selectbox("Select Activty", activities)
    if choice == "Registration":
        val=False
        with st.form("my_form"):
            st.write("Registration for the game")
            user_name = st.text_input('User Name', 'format:Type here')
            global email_id
            email_id = st.text_input('Email_id', 'xyz@mailbox.com')

            phone_number=st.text_input('Phone_number', 'format:XXXXXXXXXX')
            dob = st.text_input('Date of birth', 'format:DD-MM-YYYY')
            submitted = st.form_submit_button("Submit")
            if submitted:
                print("Submitted")
                condition=True
                d=check(email_id,dob,phone_number)
                for i in d:
                    if(not(d[i][0])):
                        wrong=i
                        condition=False
                        break
                if(condition):
                    val=insert_data(email_id,user_name,phone_number,dob)
                else:
                    st.warning("check credential and format {}".format(wrong))
        if(val):
            st.write("Detials Updates in DB")
            st.button("Launch the game",key=None, help=None, on_click=main_game())
            print(user_name,email_id,phone_number,dob)
        st.write("copyrights 2022 @ Ashish Solution")
if __name__ == '__main__':
    main()
