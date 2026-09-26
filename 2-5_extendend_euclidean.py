def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd_val, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd_val, x, y
 
if __name__ == "__main__":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
 
    gcd_val, x, y = extended_gcd(a, b)
 
    print(f"GCD({a}, {b}) = {gcd_val}")
    print(f"Coefficients: x = {x}, y = {y}")
    print(f"Verification: {a}*{x} + {b}*{y} = {a*x + b*y}")
 