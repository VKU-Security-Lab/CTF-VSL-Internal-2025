import os, random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import bytes_to_long, getPrime
a = b'\x1dE%\xec\xb9\xa4\xf5\x89\xce\xdd\x16\xdc\x89\xfc\xa3\xe1'
iv = bytes.fromhex("d0c05440bbd86e1ed2a56e8a9fc1c010")  
ciphertext = bytes.fromhex("1dc3c5d62bf6e24ec677be15d39e7e6d0a719300b45fb02ef69d167d3ec369c8d856f0c718924d45b21466680935615f")

cipher = AES.new(a, AES.MODE_CBC, iv)

plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

print("Decrypted plaintext:", plaintext.decode())