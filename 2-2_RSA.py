import random
from sympy import isprime
 
def generate_prime(bits=8):
    while True:
        n = random.getrandbits(bits) | 1
        if isprime(n):
            return n
 
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
 
def mod_inverse(e, phi):
    return pow(e, -1, phi)
 
def rsa_keygen(bits=8):
    p = generate_prime(bits)
    q = generate_prime(bits)
    while q == p:
        q = generate_prime(bits)
 
    n = p * q
    phi = (p - 1) * (q - 1)
 
    e = 65537 if phi > 65537 else 3
    while gcd(e, phi) != 1:
        e += 2
 
    d = mod_inverse(e, phi)
    return (e, n), (d, n)
 
def rsa_encrypt(m, public_key):
    e, n = public_key
    return pow(m, e, n)
 
def rsa_decrypt(c, private_key):
    d, n = private_key
    return pow(c, d, n)
 
if __name__ == "__main__":
    public_key, private_key = rsa_keygen(bits=8)
    print("Public Key (e, n):", public_key)
    print("Private Key (d, n):", private_key)
 
    m = int(input(f"Enter a message number (less than {public_key[1]}): "))
 
    c = rsa_encrypt(m, public_key)
    dec = rsa_decrypt(c, private_key)
 
    print("Encrypted:", c)
    print("Decrypted:", dec)
 