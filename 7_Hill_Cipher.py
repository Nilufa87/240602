import numpy as np
 
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
 
def matrix_mod_inverse(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det % modulus, modulus)
    if det_inv is None:
        raise ValueError("Key matrix is not invertible mod 26")
    adjugate = np.array([[matrix[1][1], -matrix[0][1]],
                          [-matrix[1][0], matrix[0][0]]])
    inverse = (det_inv * adjugate) % modulus
    return inverse
 
def text_to_numbers(text):
    return [ord(ch) - 65 for ch in text.upper() if ch.isalpha()]
 
def numbers_to_text(numbers):
    return ''.join(chr(int(n) % 26 + 65) for n in numbers)
 
def hill_encrypt(text, key_matrix):
    nums = text_to_numbers(text)
    if len(nums) % 2 != 0:
        nums.append(ord('X') - 65)  # padding
    cipher_nums = []
    for i in range(0, len(nums), 2):
        pair = np.array([[nums[i]], [nums[i+1]]])
        result = np.dot(key_matrix, pair) % 26
        cipher_nums.extend(result.flatten())
    return numbers_to_text(cipher_nums)
 
def hill_decrypt(cipher, key_matrix):
    inverse_matrix = matrix_mod_inverse(key_matrix, 26)
    nums = text_to_numbers(cipher)
    plain_nums = []
    for i in range(0, len(nums), 2):
        pair = np.array([[nums[i]], [nums[i+1]]])
        result = np.dot(inverse_matrix, pair) % 26
        plain_nums.extend(result.flatten())
    return numbers_to_text(plain_nums)
 
if __name__ == "__main__":
    # Example key matrix (must be invertible mod 26)
    key_matrix = np.array([[3, 3], [2, 5]])
 
    msg = input("Enter message (letters only): ")
 
    enc = hill_encrypt(msg, key_matrix)
    dec = hill_decrypt(enc, key_matrix)
 
    print("Key Matrix:\n", key_matrix)
    print("Encrypted:", enc)
    print("Decrypted:", dec)
 