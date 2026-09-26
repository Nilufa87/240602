def caesar_decrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 - shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 - shift) % 26 + 97)
        else:
            result += ch
    return result
 
def brute_force(cipher):
    print("Trying all 26 possible keys:\n")
    for key in range(26):
        print(f"Key {key:2d}: {caesar_decrypt(cipher, key)}")
 
if __name__ == "__main__":
    cipher = input("Enter Caesar cipher encrypted text: ")
    brute_force(cipher)
 