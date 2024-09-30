import streamlit as st
import time
import streamlit as st

def check_login():
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False

def login(username, password):
    if username == "lap" and password == "123":
        st.session_state['logged_in'] = True
        st.success("Đăng nhập thành công!")
        time.sleep(2)
        st.rerun()
    else:
        st.error("Thông tin đăng nhập không chính xác!")

def logout():
    st.session_state['logged_in'] = False
    st.success("Đăng xuất thành công!")
    time.sleep(1)
    st.rerun()

