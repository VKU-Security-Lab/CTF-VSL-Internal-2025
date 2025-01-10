from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random
import sys
import os

secret_len = 4

def get_encrypted_flag(key):
    flag = os.environ["FLAG"]
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(flag.encode(), 16)).hex()


def main():
    secret = os.urandom(secret_len)
    secret_bin = bin(int.from_bytes(secret, "big"))[2:].zfill(secret_len*8)

    print(f"Encrypted flag: {get_encrypted_flag(secret*(16//secret_len))}")

    while True:
        exp = input("Enter expression: ")
        assert "exec" not in exp

        chosen = random.randint(0, 2**len(secret_bin) - 1)
        old = sys.stdout
        sys.stdout = open(os.devnull, 'w')
        for i in range(len(secret_bin)):
            if (chosen >> i) & 1:
                eval(exp, {'c': secret_bin[i]})
        sys.stdout = old
        print(f"{chosen = }")

if __name__ == "__main__":
    main()