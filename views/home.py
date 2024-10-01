import streamlit as st
import time
from views import chat

def show():
    # Tạo thanh điều hướng ở bên trái
    st.sidebar.title("Trang chủ")
    page = st.sidebar.selectbox("Vui lòng chọn chức năng mà bạn muốn sử dụng", ("Chatbot", "Giới Thiệu", "Liên Hệ"))

    if 'home' not in st.session_state:
        st.session_state.home = "Chat"  # Khởi tạo giá trị mặc định

    # Selectbox để chọn giữa đăng nhập và đăng ký
    if st.session_state.home == "Chat":
        chat.show()  # Gọi hàm login