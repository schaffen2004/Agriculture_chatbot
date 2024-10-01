import streamlit as st
import time
from utils import authenticate
from models import account

def show():
    st.title("Đăng ký")
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type='password')
    confirmPassword = st.text_input("Nhập lại mật khẩu", type='password')
    # Định nghĩa CSS để căn chỉnh button
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
    if st.button("Đăng ký"):
        if authenticate.check_register(username, password,confirmPassword):
            account.add_account(username,password)
            st.success("Đăng ký thành công!")
            st.session_state.page = "Login"  # Chuyển sang trang chính
            time.sleep(1.5)
            st.rerun()
        else:
            st.error("Vui lòng kiểm tra lại thông tin đăng ký.")
            time.sleep(1.5)
            st.rerun()
    
    if st.button("Trở lại đăng nhập",type="secondary"):
        st.session_state.page = "Login"
        st.rerun()