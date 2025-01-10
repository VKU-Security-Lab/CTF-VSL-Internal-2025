import os, random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import bytes_to_long, getPrime

def random_bytes(length):
    return os.urandom(length)

key_length = 16  
num_keys = 5   
K_main = random_bytes(key_length)
K_main_enc=K_main + b'<--- this key'


p = getPrime(1024) 
e = 65537
while (p - 1) % e == 0:
    p = getPrime(1024)
Number = []
while len(Number)<4:
    q = getPrime(2048)
    n = p * q
    if (q - 1) % e != 0 and n not in Number:
	    Number.append(n)
K_main_enc += os.urandom(2048 // 8 - 2 - len(K_main_enc))
K_main_enc = bytes_to_long(K_main_enc)

scrambled_keys= [pow(K_main_enc, e, n) for n in Number]
Number = [N + int(os.urandom(32).hex(), 16) for N in Number]
random.shuffle(Number)


plaintext = b"VSL{AES_and_crypto_is_not_easy!!!}"
cipher = AES.new(K_main, AES.MODE_CBC)
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

iv = cipher.iv
print("Ciphertext (hex):", ciphertext.hex())
print("IV (hex):", iv.hex())
print("Scrambled keys =", [key for key in scrambled_keys])
print("Number= ", Number)

