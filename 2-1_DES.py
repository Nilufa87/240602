# Requires: pip install pycryptodome
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
 
def des_encrypt(message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    ct = cipher.encrypt(pad(message.encode(), DES.block_size))
    return ct
 
def des_decrypt(ct, key):
    cipher = DES.new(key, DES.MODE_ECB)
    pt = unpad(cipher.decrypt(ct), DES.block_size)
    return pt.decode()
 
if __name__ == "__main__":
    key = b"8bytekey"  # DES key must be exactly 8 bytes
    msg = input("Enter message: ")
 
    ct = des_encrypt(msg, key)
    dec = des_decrypt(ct, key)
 
    print("Encrypted (hex):", ct.hex())
    print("Decrypted:", dec)