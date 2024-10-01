import streamlit as st
import google.generativeai as genai


def chatbot_response(chat,message, history):
    # Thêm câu hỏi vào lịch sử
    history.append((message, ""))

    # Prompt hệ thống để hướng dẫn chatbot trả lời liên quan đến nông nghiệp bằng tiếng Việt
    system_message = "Bạn là một chuyên gia về nông nghiệp ở Việt Nam. Hãy trả lời các câu hỏi liên quan đến trồng trọt, chăn nuôi, đánh bắt thuỷ sản, đất đai, thời tiết và các kỹ thuật nông nghiệp khác ở Việt Nam. Trả lời ngắn gọn và chính xác bằng tiếng Việt. Không nêu thêm thông tin bổ sung cho câu hỏi."

    response = chat.send_message(message, stream=True)
    chatbot_reply = ""
    for chunk in response:
        if chunk.text:
          chatbot_reply += chunk.text + " "

    # Cập nhật lịch sử với câu trả lời
    history[-1] = (message, chatbot_reply)

    return history  # Trả về lịch sử

def show():
    # Set the base URL and API key for the OpenAI client
    genai.configure(api_key='AIzaSyBqHLvnvATwKlnQEhmJQxM_BSAQolc0hg4')
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])

    # Giao diện Streamlit
    st.title("Chatbot Nông Nghiệp")

    # Khởi tạo hoặc lấy lịch sử trò chuyện
    if 'history' not in st.session_state:
        st.session_state.history = []

    # Tạo vùng cuộn để hiển thị lịch sử trò chuyện
    st.subheader("Lịch sử trò chuyện")

    # Vùng cuộn cho lịch sử trò chuyện
    chat_area = st.container()
    with chat_area:
        # Hiển thị lịch sử trò chuyện trong một vùng cuộn
        if st.session_state.history:
            for user_message, bot_reply in st.session_state.history:
                st.chat_message("user").markdown(user_message)
                st.chat_message("assistant").markdown(bot_reply)
        else:
            st.markdown("Chưa có lịch sử trò chuyện.")

    # Ô nhập liệu cho người dùng
    user_input = st.text_input("Nhập câu hỏi của bạn...", "")

    # Nút gửi
    if st.button("Gửi"):
        if user_input:
            # Gọi hàm xử lý phản hồi và cập nhật lịch sử
            st.session_state.history = chatbot_response(chat,user_input, st.session_state.history)

            # Làm trống ô nhập liệu
            st.text_input("Nhập câu hỏi của bạn...", "", key="new_input")
            st.rerun()
            # Cập nhật lại lịch sử trò chuyện
            with chat_area:
                for user_message, bot_reply in st.session_state.history:
                    st.chat_message("user").markdown(user_message)
                    st.chat_message("assistant").markdown(bot_reply)

