from models import account

def check_login(username, password):
    # Giả sử kiểm tra thông tin đăng nhập (có thể thay thế bằng logic thực tế)
    return account.check_account_credentials(username,password)

def check_account(username):
    return account.account_exists(username)

def check_register(username,password,confirmPassword):
    if password != confirmPassword:
        return False
    elif account.account_exists(username):
        return False
    return True
