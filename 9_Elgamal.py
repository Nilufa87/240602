import random
from sympy import isprime, primitive_root
 
def generate_prime(bits=8):
    while True:
        n = random.getrandbits(bits) | 1
        if isprime(n):
            return n
 
def elgamal_keygen(bits=8):
    p = generate_prime(bits)
    g = primitive_root(p)
    x = random.randint(2, p - 2)          # private key
    h = pow(g, x, p)                      # public key component
    return p, g, h, x
 
def elgamal_encrypt(p, g, h, m):
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    c2 = (m * pow(h, k, p)) % p
    return c1, c2
 
def elgamal_decrypt(p, x, c1, c2):
    s = pow(c1, x, p)
    s_inv = pow(s, -1, p)
    m = (c2 * s_inv) % p
    return m
 
if __name__ == "__main__":
    p, g, h, x = elgamal_keygen(bits=8)
    print(f"Public Key: p={p}, g={g}, h={h}")
    print(f"Private Key: x={x}")
 
    m = int(input(f"Enter a message number (less than {p}): "))
 
    c1, c2 = elgamal_encrypt(p, g, h, m)
    dec = elgamal_decrypt(p, x, c1, c2)
 
    print("Encrypted:", (c1, c2))
    print("Decrypted:", dec)
 