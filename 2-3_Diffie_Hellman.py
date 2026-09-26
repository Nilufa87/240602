import random
 
def diffie_hellman(p, g):
    # Private keys
    a = random.randint(2, p - 2)   # Alice's private key
    b = random.randint(2, p - 2)   # Bob's private key
 
    # Public keys
    A = pow(g, a, p)               # Alice sends A to Bob
    B = pow(g, b, p)               # Bob sends B to Alice
 
    # Shared secret computed independently
    shared_alice = pow(B, a, p)
    shared_bob = pow(A, b, p)
 
    return a, b, A, B, shared_alice, shared_bob
 
if __name__ == "__main__":
    p = int(input("Enter a prime number p: "))
    g = int(input("Enter a primitive root g: "))
 
    a, b, A, B, shared_alice, shared_bob = diffie_hellman(p, g)
 
    print(f"\nAlice's private key: {a}, public key: {A}")
    print(f"Bob's private key:   {b}, public key: {B}")
    print(f"\nAlice computes shared secret: {shared_alice}")
    print(f"Bob computes shared secret:   {shared_bob}")
 
    if shared_alice == shared_bob:
        print("\nKey exchange successful! Shared secret:", shared_alice)
    else:
        print("\nKey exchange failed.")
 