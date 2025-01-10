import hashlib
import random
import os

BLOCK_SIZE = 8
CHECK_SIZE = 2
KEY = [random.randbytes(32) for _ in range(BLOCK_SIZE + CHECK_SIZE)]

def encrypt_block(block, key):
    assert len(block) == BLOCK_SIZE

    ciphertext = []
    checksum = 0

    for i in range(BLOCK_SIZE):
        state = hashlib.sha256(key[i]).digest()
        for _ in range(block[i]):
            state = hashlib.sha256(state).digest()
        ciphertext.append(state.hex())
        checksum += (255 - block[i])

    checksum_bytes = int.to_bytes(checksum, 2, byteorder='little')
    for i in range(CHECK_SIZE):
        state = hashlib.sha256(key[i + BLOCK_SIZE]).digest()
        for _ in range(checksum_bytes[i]):
            state = hashlib.sha256(state).digest()
        ciphertext.append(state.hex())
    
    return ciphertext
        
def pad(msg):
    return msg + b"\x00"*(- len(msg) % BLOCK_SIZE)

def encrypt(msg, key):
    padded_msg = pad(msg)

    ciphertext = []
    for i in range(0, len(msg), BLOCK_SIZE):
        ciphertext += encrypt_block(padded_msg[i: i + BLOCK_SIZE], key)
    
    return ciphertext


def decrypt_block(block, key):
    assert len(block) == BLOCK_SIZE + CHECK_SIZE
    
    plaintext = []
    checksum = 0
    
    for i in range(BLOCK_SIZE):
        state = key[i]
        for c in range(256):
            state = hashlib.sha256(state).digest()
            if (state.hex() == block[i]):
                break
        plaintext.append(c)
        checksum += (255 - c)

    checksum_bytes = int.to_bytes(checksum, 2, byteorder='little')
    for i in range(CHECK_SIZE):
        state = hashlib.sha256(key[i + BLOCK_SIZE]).digest()
        for _ in range(checksum_bytes[i]):
            state = hashlib.sha256(state).digest()
        assert state.hex() == block[BLOCK_SIZE + i], "Invalid checksum"
    
    return bytes(plaintext)

def decrypt(msg, key):
    plaintext = b""
    for i in range(0, len(msg), BLOCK_SIZE + CHECK_SIZE):
        plaintext += decrypt_block(msg[i: i + BLOCK_SIZE + CHECK_SIZE], key)
    return plaintext

def main():
    print(f"Last key: {KEY[-1].hex()}")
    your_msg = bytes.fromhex(input("Enter message: "))
    assert len(your_msg) <= 8
    print(f"Encrypted message: {encrypt(your_msg, KEY)}")
    order = decrypt(eval(input("Give me a order: "), {'__builtins__': None}, {}), KEY)

    if order == b"give me the flag":
        print(f"This is flag: {os.environ['FLAG']}")

if __name__ == "__main__":
    main()