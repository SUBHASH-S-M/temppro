from game_prog import *
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import os
from db_operations import *

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

def game():
    pass
def main():
    local_css("style.css")
    activities = [ "Registration","ABOUT"]
    choice = st.sidebar.selectbox("Select Activty", activities)
    if choice == "Registration":
        val=False
        with st.form("my_form"):
            st.write("Registration for the game")
            user_name = st.text_input('User Name', 'format:Type here')
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
            st.button("Launch the game",key=None, help=None, on_click=game())
            print(user_name,email_id,phone_number,dob)
        st.write("copyrights 2022 @ Ashish Solution")
if __name__ == '__main__':
    main()
