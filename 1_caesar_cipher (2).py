def caesar_encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch
    return result
 
def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)
 
if __name__ == "__main__":
    msg = input("Enter message: ")
    key = int(input("Enter shift key: "))
 
    enc = caesar_encrypt(msg, key)
    dec = caesar_decrypt(enc, key)
 
    print("Encrypted:", enc)
    print("Decrypted:", dec)
 