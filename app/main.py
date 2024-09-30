# app/main.py
import streamlit as st
from forms import login
import time
from PIL import Image

def main():
    login.check_login()
    
    if st.session_state['logged_in']:
        st.write("Chào mừng bạn đến với ứng dụng!")
        if st.button("Đăng xuất"):
            login.logout()
    else:
        st.title("Đăng Nhập")
        username = st.text_input("Tên đăng nhập")
        password = st.text_input("Mật khẩu", type="password")
        
        if st.button("Đăng Nhập"):
            login.login(username, password)

    

if __name__ == '__main__':
    main()