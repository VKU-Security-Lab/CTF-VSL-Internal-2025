import mysql.connector

# Kết nối tới cơ sở dữ liệu MySQL
connection = mysql.connector.connect(
    host='localhost',  # Địa chỉ của MySQL server (localhost nếu trên máy tính cục bộ)
    user='root',  # Tên người dùng (root nếu sử dụng tài khoản root)
    password='',  # Mật khẩu của tài khoản root
    database='test'  # Tên cơ sở dữ liệu cần kết nối
)

# Tạo một đối tượng cursor để thực hiện các truy vấn SQL
cursor = connection.cursor()

# Dữ liệu người dùng mới
name = "John Doe"
email = "john.doe@example.com"
password = "securepassword"
username = "johndoe"
avatar = "avatar_url"
is_active = True

# Lệnh SQL để thêm người dùng mới
insert_query = """
INSERT INTO users (name, email, password, username, avatar, is_active)
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Thực thi lệnh SQL với dữ liệu người dùng mới
cursor.execute(insert_query, (name, email, password, username, avatar, is_active))

# Lưu thay đổi vào cơ sở dữ liệu
connection.commit()

# In ra thông báo
print("User added successfully!")

# Đóng kết nối
cursor.close()
connection.close()
