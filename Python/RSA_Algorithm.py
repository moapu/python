def encrypt( plaintext, e, n ):
    return (plaintext ** e) % n

def decrypt( c, d, n ):
    return (c ** d) % n

def main():
    p = 11
    q = 13
    n = p * q
    m = (p - 1) * (q - 1)
    e = 7
    d = 103
    p_text = 9
    cipher_text = encrypt( p_text, e, n )
    decrypted_text = decrypt( cipher_text, d, n )

    # Encryption Process
    print('User Chose:')
    print(f'\tP = {p}')
    print(f'\tQ = {q}')
    print(f'\tN = P x Q = {n}')
    print(f'\tPublic Key(e) = {e}')
    print(f'\tPrivate Key(d) = {d}')
    print(f'\tϕ(n) = (p−1) x (q−1) = {m}')
    print(f'\tPlaintext: {p_text}')

    print("\nEncrypting...")
    print("\tEquation: M^e mod n = C")
    print(f'\tCiphertext: {cipher_text}')
    print("\nDecrypting...")
    print("\tEquation: C^d mod n = M")
    print(f'\tPlaintext: {decrypted_text}')

if __name__ == '__main__':
    main()
