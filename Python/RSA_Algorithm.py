import math


def encrypt(plaintext, e, n):
    return (plaintext ** e) % n


def decrypt(c, d, n):
    return (c ** d) % n


def isPrime(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
        else:
            return True


def main():
    prime_nums = [2, 3, 5, 7, 11, 13,
                  17, 19, 23, 29, 31,
                  37, 41, 43, 47, 53,
                  59, 61, 67, 71, 73,
                  79, 83, 89, 97, 101,
                  103, 107, 109, 113,
                  127, 131, 137, 139,
                  149, 151, 157, 163,
                  167, 173, 179, 181,
                  191, 193, 197, 199]
    candidate_e = []

    print("Enter 2 prime numbers: ")
    print("P: ", end=" ")
    p = int(input())

    while p not in prime_nums:
        print("P: ", end=" ")
        p = int(input())

    print("Q: ", end=" ")
    q = int(input())

    while q not in prime_nums:
        print("Q: ", end=" ")
        q = int(input())

    print("\nCandidate e:")
    n = p * q
    m = (p - 1) * (q - 1)

    for i in range(1, m + 1):
        if math.gcd(m, i) == 1:
            candidate_e.append(i)
            print(f'{i}', end=" ")

    print("\n")
    e = int(input('Choose e >> '))
    while e not in candidate_e:
        e = int(input('Choose e >> '))

    d = 0
    print("Determine d >> ", end=" ")
    for i in range(1, m + 1):
        if (i * e) % m == 1 and i < m:
            d = i
    print(d)
    print(f"Key Pair: ({e} {n}) ({d} {n})")

    plain_text = input("Plain Text >> ")

    c = encrypt(int(plain_text), e, n)
    print(f"Cipher Text: {c}")

    decrypted_text = decrypt(c, d, n)
    print(f"Decrypted Text >> {decrypted_text}")


if __name__ == '__main__':
    main()
