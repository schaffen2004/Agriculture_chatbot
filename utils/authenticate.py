from models import account

def check_login(username, password):
    # Giả sử kiểm tra thông tin đăng nhập (có thể thay thế bằng logic thực tế)
    return account.check_account_credentials(username,password)