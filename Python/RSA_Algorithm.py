import math


# Lists all the e candidates
def list_candidates(m):
    candidate = []
    for i in range(1, m + 1):
        if math.gcd(m, i) == 1:
            candidate.append(i)
            print(f'{i}', end=" ")

    return candidate


# determine the decryption key
def determine_d(m, e):
    d = 0
    for i in range(1, m + 1):
        if (i * e) % m == 1 and i < m:
            d = i

    return d


# encrypt the plaintext
def encrypt(plaintext, e, n):
    return (plaintext ** e) % n


# decrypt the cipher text
def decrypt(c, d, n):
    return (c ** d) % n


# is it a prime number?
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True


# validates if its a prime number
def prime_num_validation(chr):
    print(f'{chr}:', end=" ")
    n = int(input())

    while not is_prime(n):
        print(f"{chr}: ", end=" ")
        n = int(input())

    return n


def main():
    # prompt
    print("Enter 2 prime numbers: ")

    # prompt for P, Q
    p = prime_num_validation("P")
    q = prime_num_validation("Q")

    # candidate for e
    print("\nCandidate e:")
    d = 0
    n = p * q
    m = (p - 1) * (q - 1)

    # list of e candidates
    candidate_e = list_candidates(m)

    print("\n")

    # prompt to choose e
    e = int(input('Choose e >> '))
    while e not in candidate_e:
        e = int(input('Choose e >> '))

    # determine d
    d = determine_d(m, e)
    print(f"Determine d >> {d}")

    # print Key pair
    print(f"Key Pair: ({e} {n}) ({d} {n})")

    # prompt for Plain Text
    plain_text = input("Plain Text >> ")
    while not plain_text.isdigit():
        plain_text = input("Plain Text >> ")

    c = encrypt(int(plain_text), e, n)
    print(f"Cipher Text: {c}")

    decrypt_text = decrypt(c, d, n)
    print(f"Decrypted Text >> {decrypt_text}")


if __name__ == '__main__':
    main()
