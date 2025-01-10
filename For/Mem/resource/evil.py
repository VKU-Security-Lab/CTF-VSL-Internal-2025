import os
import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

password = input("Enter the password: ")
salt = get_random_bytes(16)
key = scrypt(password, salt, key_len=32, N=16384, r=8, p=1)
cipher = AES.new(key, AES.MODE_CBC)

directory = os.getcwd()

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)
    if os.path.isfile(file_path) and not filename.endswith('.vsl'): 
        with open(file_path, 'rb') as file:
            file_data = file.read()

        encrypted_data = cipher.encrypt(pad(file_data, AES.block_size))
        encrypted_data_b64 = base64.b64encode(salt + cipher.iv + encrypted_data)

        with open(file_path + '.vsl', 'wb') as file:
            file.write(encrypted_data_b64)
        os.remove(file_path)
        print("File has been encrypted and saved as " + file_path + ".vsl")
