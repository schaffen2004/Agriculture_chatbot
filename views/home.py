import streamlit as st
import time
from views import chat, prediction,eda
def show():
    # Tạo thanh điều hướng ở sidebar
    st.sidebar.title("Trang chủ")
    page = st.sidebar.selectbox("Vui lòng chọn chức năng mà bạn muốn sử dụng", 
                                ("Chatbot", "Trực quan hoá dữ liệu","Dự đoán"))

    # Điều hướng giữa các trang
    if page == "Chatbot":
        chat.show()

    elif page == "Trực quan hoá dữ liệu":
        eda.show()

    elif page == "Dự đoán":
        prediction.show()
 

    