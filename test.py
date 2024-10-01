
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://laphv494:oS4tGn8sR9v5oKqh@agrichatbot.c2z5m.mongodb.net/?retryWrites=true&w=majority&appName=AgriChatbot"

# Create a new client and connect to the server
client = MongoClient(uri)


# Chọn cơ sở dữ liệu
db = client['chatbot']

# Chọn collection trong cơ sở dữ liệu
collection = db['account']  # Thay đổi tên collection của bạn

# Tài liệu mới để chèn vào
new_document = {
    "user": "lap",
    "pass": "123",
}

# Chèn tài liệu vào collection
insert_result = collection.insert_one(new_document)

# In ra ObjectId của tài liệu vừa chèn
print("Inserted document ID:", insert_result.inserted_id)

# Đóng kết nối
client.close()