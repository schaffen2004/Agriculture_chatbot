import streamlit as st
import time
from utils import authenticate

def show():

    st.title("Đăng nhập")
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type='password')
    button_style = """
        <style>
        div.stButton > button {
        width : 100%;
        border-radius: 10px;
    }

    div.stButton > button:hover {
        width : 100%;
    }
        </style>
    """

    # Đưa CSS vào giao diện
    st.markdown(button_style, unsafe_allow_html=True)
    if st.button("Đăng nhập"):
        if authenticate.check_login(username, password):
            st.success("Đăng nhập thành công!")
            st.session_state.page = "Home"  # Chuyển sang trang chính
            time.sleep(1.5)
            st.rerun()
        else:
            st.error("Vui lòng kiểm tra lại tên đăng nhập và mật khẩu.")
            time.sleep(1.5)
            st.rerun()
    
    if st.button("Đăng ký"):
        st.session_state.page = "Register"
        st.rerun()