from pymongo import MongoClient


def check_account_credentials(username, password):
    # Kết nối tới MongoDB Atlas
    uri = "mongodb+srv://laphv494:oS4tGn8sR9v5oKqh@agrichatbot.c2z5m.mongodb.net/?retryWrites=true&w=majority&appName=AgriChatbot"
    client = MongoClient(uri)

    # Chọn cơ sở dữ liệu
    db = client['chatbot']

    # Chọn collection trong cơ sở dữ liệu
    collection = db['account']  # Thay đổi tên collection của bạn

    # Tìm tài khoản trong collection
    user_document = collection.find_one({"user": username})

    # Đóng kết nối
    client.close()

    # Kiểm tra xem tài khoản đã tồn tại và mật khẩu có khớp không
    if user_document and user_document.get("pass") == password:
        return True  # Tài khoản và mật khẩu đúng
    else:
        return False  # Tài khoản không tồn tại hoặc mật khẩu sai

def account_exists(username):
    # Kết nối tới MongoDB Atlas
    uri = "mongodb+srv://laphv494:oS4tGn8sR9v5oKqh@agrichatbot.c2z5m.mongodb.net/?retryWrites=true&w=majority&appName=AgriChatbot"
    client = MongoClient(uri)

    # Chọn cơ sở dữ liệu
    db = client['chatbot']

    # Chọn collection trong cơ sở dữ liệu
    collection = db['account']  # Thay đổi tên collection của bạn

    # Kiểm tra xem tài khoản đã tồn tại chưa
    existing_user = collection.find_one({"user": username})

    # Đóng kết nối
    client.close()

    return existing_user is not None

def add_account(username,password):
    uri = "mongodb+srv://laphv494:oS4tGn8sR9v5oKqh@agrichatbot.c2z5m.mongodb.net/?retryWrites=true&w=majority&appName=AgriChatbot"

    # Create a new client and connect to the server
    client = MongoClient(uri)


    # Chọn cơ sở dữ liệu
    db = client['chatbot']

    # Chọn collection trong cơ sở dữ liệu
    collection = db['account']  # Thay đổi tên collection của bạn

    # Tài liệu mới để chèn vào
    new_document = {
        "user": username,
        "pass": password,
    }

    # Chèn tài liệu vào collection
    insert_result = collection.insert_one(new_document)

    # In ra ObjectId của tài liệu vừa chèn
    print("Inserted document ID:", insert_result.inserted_id)

    # Đóng kết nối
    client.close()
