import os
import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Util.Padding import unpad

password = input("Enter the password: ")
encrypted_file_path = 'secret.txt.vsl'

with open(encrypted_file_path, 'rb') as file:
    encrypted_data_b64 = file.read()

encrypted_data = base64.b64decode(encrypted_data_b64)
salt = encrypted_data[:16]
iv = encrypted_data[16:32]
encrypted_data = encrypted_data[32:]
key = scrypt(password, salt, key_len=32, N=16384, r=8, p=1)
cipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

with open('decrypted_secret.txt', 'wb') as file:
    file.write(decrypted_data)

print("File has been decrypted and saved as decrypted_secret.txt")
