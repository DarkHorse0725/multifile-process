from main import main
import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()


def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')


def add_userdata(username, password):
    c.execute('INSERT INTO userstable(username, password) VALUES (?,?)',
              (username, password))
    conn.commit()


def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?',
              (username, password))
    data = c.fetchall()
    return data


def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data


def login_interface():
    menu = ['Login', 'SignUp']
    signin_css = '''
                <style>
                    button[kind="primary"] {
                        position: fixed;
                        top: 50px;
                        right: 250px;
                        z-index: 999999;
                    }
                    button[kind="secondary"] {
                        position: fixed;
                        top: 50px;
                        right: 150px;
                        z-index: 999999;
                    }
                </style>
                '''
    st.markdown(signin_css, unsafe_allow_html=True)
    if st.button("Sign In", key=2, type="primary"):
        username = st.text_input('User Name', key='s-1')
        password = st.text_input('Password', key='s-2', type='password')
        create_usertable()
        result = login_user(username, password)
        if result:
            st.session_state["user"] = username
            custom_css = '''
                <style>
                    div.row-widget.stSelectbox {
                        display: none;
                    }
                    div.row-widget.stTextInput.css-m7ldf1.e1q7aese0{
                        display: none;
                    }
                </style>
                '''
            st.markdown(custom_css, unsafe_allow_html=True)
            main()
            
            print(st.session_state.user)
        else:
            st.warning("Invalid Username or Password")


    st.button("Sign Up", key=1)
    choice = st.sidebar.selectbox('Menu', menu)
    if len(st.session_state.user) > 0:
        main()
    # if choice == 'Login' and len(st.session_state.user) == 0:
    #     username = st.sidebar.text_input('User Name')
    #     password = st.sidebar.text_input('Password', type='password')

    #     if st.sidebar.checkbox('Login'):
    #         create_usertable()
    #         result = login_user(username, password)
    #         if result:
    #             st.session_state["user"] = username
    #             custom_css = '''
    #                 <style>
    #                     div.row-widget.stSelectbox {
    #                         display: none;
    #                     }
    #                     div.row-widget.stTextInput.css-m7ldf1.e1q7aese0{
    #                         display: none;
    #                     }
    #                 </style>
    #                 '''
    #             st.markdown(custom_css, unsafe_allow_html=True)
    #             main()
                
    #             print(st.session_state.user)
    #         else:
    #             st.warning("Invalid Username or Password")

    # elif choice == 'SignUp' and len(st.session_state.user) == 0:
    #     st.subheader('Create new account')
    #     new_user = st.text_input("Usename")
    #     new_password = st.text_input("Password", type='password')

    #     if st.button("Signup"):
    #         create_usertable()
    #         add_userdata(new_user, new_password)
    #         st.success("You have successfully created an accoount")
    #         st.info("Go to Login Menu to Log in to your account.")


if __name__ == '__main__':
    st.session_state.user = ''
    if len(st.session_state.user) > 0:
        main()
    else:
        login_interface()
