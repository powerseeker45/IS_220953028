# Implement the Paillier encryption scheme in Python. Encrypt two integers (e.g., 15 and 25) 
# using your implementation of the Paillier encryption scheme. Print the ciphertexts. Perform 
# an addition operation on the encrypted integers without decrypting them. Print the result of 
# the addition in encrypted form. Decrypt the result of the addition and verify that it matches 
# the sum of the original integers.


from Crypto.Util import number
import random

#Generates a public/private key pair for Paillier encryption
def generate_keypair(bits=512):
    p = number.getPrime(bits)
    q = number.getPrime(bits)
    n = p * q
    g = n + 1  # g = n + 1 is often used in practical implementations
    lambda_n = (p - 1) * (q - 1)  # λ(n) = (p - 1)(q - 1)
    mu = number.inverse(lambda_n, n)  # Modular inverse of λ(n) modulo n
    return (n, g), (lambda_n, mu)

#Encrypts a message using the Paillier encryption scheme
def encrypt(public_key, message):
    n, g = public_key
    r = random.randint(1, n - 1)  # Random value for encryption
    ciphertext = (pow(g, message, n * n) * pow(r, n, n * n)) % (n * n)
    return ciphertext

#Decrypts a ciphertext using the Paillier encryption scheme
def decrypt(private_key, public_key, ciphertext):
    n, g = public_key
    lambda_n, mu = private_key
    u = pow(ciphertext, lambda_n, n * n)
    low = (u - 1) // n
    message = (low * mu) % n
    return message


# Generate key pair
public_key, private_key = generate_keypair(bits=512)

# Encrypt integers
a = 15
b = 25
ciphertext_a = encrypt(public_key, a)
ciphertext_b = encrypt(public_key, b)

# Perform additive homomorphic operation (add ciphertexts)
ciphertext_sum = (ciphertext_a * ciphertext_b) % (public_key[0] * public_key[0])

# Decrypt the result
decrypted_sum = decrypt(private_key, public_key, ciphertext_sum)

# Print results
print(f"Ciphertext of a: {ciphertext_a}")
print(f"Ciphertext of b: {ciphertext_b}")
print(f"Ciphertext of a + b: {ciphertext_sum}")
print(f"Decrypted sum: {decrypted_sum}")
print(f"Expected sum: {a + b}")

