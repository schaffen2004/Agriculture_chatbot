import streamlit as st
from views import  login,register,home

# Giao diện chính
def main():
    # Kiểm tra xem page đã được khởi tạo chưa
    if 'page' not in st.session_state:
        st.session_state.page = "Login"  # Khởi tạo giá trị mặc định

    # Selectbox để chọn giữa đăng nhập và đăng ký
    if st.session_state.page == "Login":
        login.show()  # Gọi hàm login
    elif st.session_state.page == "Register":
        register.show()  # Gọi hàm register
    elif st.session_state.page == "Home":
        home.show()  # Gọi hàm home

# Gọi hàm main để chạy
if __name__ == "__main__":
    main()

