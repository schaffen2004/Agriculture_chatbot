import streamlit as st
import time
from views import chat, prediction
def show():
    # Tạo thanh điều hướng ở sidebar
    st.sidebar.title("Trang chủ")
    page = st.sidebar.selectbox("Vui lòng chọn chức năng mà bạn muốn sử dụng", 
                                ("Chatbot", "Dự đoán"))

    # Điều hướng giữa các trang
    if page == "Chatbot":
        chat.show()


    elif page == "Dự đoán":
        prediction.show()


    