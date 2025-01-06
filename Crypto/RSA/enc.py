from Crypto.Util import number
from Crypto.Util.number import bytes_to_long, long_to_bytes
p = number.getPrime(128)
q = number.getPrime(128)
flag = b'vsl{RSA_1s_5o_3a5y_h3h3!!}'
n = p * q
phi_n = (p - 1) * (q - 1)

e = 65537

d = pow(e, -1, phi_n)

rsa_keys = {
    "p (512-bit prime)": p,
    "q (512-bit prime)": q,
    "n (p * q)": n,
    "phi(n)": phi_n,
    "e (public exponent)": e,
    "d (private key)": d
}

print(rsa_keys)
print(f'ciphertext: {pow(bytes_to_long(flag), e, n)}')

print(f'plaintext: {long_to_bytes(pow(pow(bytes_to_long(flag), e, n), d, n))}')