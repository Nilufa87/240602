def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
 
def find_all_primitive_roots(p):
    required_set = set(range(1, p))
    roots = []
    for g in range(2, p):
        actual_set = set(pow(g, powers) % p for powers in range(1, p))
        if actual_set == required_set:
            roots.append(g)
    return roots
 
def mod_operations(base, exponent, modulus):
    power = pow(base, exponent, modulus)
    inverse = pow(base, -1, modulus) if gcd(base, modulus) == 1 else None
    return power, inverse
 
if __name__ == "__main__":
    p = int(input("Enter a prime number p: "))
 
    roots = find_all_primitive_roots(p)
    print(f"Primitive roots of {p}:", roots)
 
    if roots:
        g = roots[0]
        base = int(input(f"\nEnter a base number (using primitive root {g}): "))
        exp = int(input("Enter an exponent: "))
 
        power, inverse = mod_operations(base, exp, p)
        print(f"{base}^{exp} mod {p} = {power}")
        print(f"Modular inverse of {base} mod {p} = {inverse}")
 