#Implement the Paillier encryption scheme in Python. 
# Encrypt two integers (e.g., 15 and 25) using your implementation of the Paillier encryption scheme. 
# Print the ciphertexts. 
# Perform an addition operation on the encrypted integers without decrypting them. 
# Print the result of the addition in encrypted form. 
# Decrypt the result of the addition and verify that it matches the sum of the original integers. 
# Extend the above scheme for multiple numbers (eg: 20,25,30,25, etc). 
# Perform scalar multiplication operation on one of the encrypted integer with 3 and print the multiplication in encrypted form. 
# Decrypt the result of the multiplication and verify that it matches the multiplication of the original integer and 3. 
# Build an inverted index mapping numbers to the list of document IDs containing those numbers (eg: 1:"45", 2:"30", 3:"35", etc). 
# Encrypt the index using the Paillier cryptosystem.
# Take a search query as input. 
# Encrypt the query using the public key. 
# Search the encrypted index for matching terms. 
# Decrypt the returned document IDs using the private key. 
# Print the corresponding Document ID for the numbers. (eg: Search query = 45. Output should be ID_1). Implement batch encryption and decryption. 
# Compare the time taken in Paillier Encryption, Homomorphic operation and Decryption for small number (eg:10) and large number(eg: 10000).

import random
import hashlib
from Crypto.Util import number

# Paillier encryption/decryption
class Paillier:
    def __init__(self, keysize=512):
        self.keysize = keysize
        self.public_key, self.private_key = self.generate_keypair()

    def generate_keypair(self):
        p = number.getPrime(self.keysize)
        q = number.getPrime(self.keysize)
        n = p * q
        g = n + 1  # In practice, g = n + 1 is commonly used
        lambda_n = (p - 1) * (q - 1)
        mu = number.inverse(lambda_n, n)  # Modular inverse
        return (n, g), (lambda_n, mu)

    def encrypt(self, pub_key, m, r=None):
        n, g = pub_key
        if r is None:
            r = random.randint(1, n - 1)  # Generate random r if not provided
        c = (pow(g, m, n * n) * pow(r, n, n * n)) % (n * n)
        return c

    def decrypt(self, priv_key, pub_key, c):
        n, _ = pub_key
        lambda_n, mu = priv_key
        u = pow(c, lambda_n, n * n)
        l = (u - 1) // n
        m = (l * mu) % n
        return m



# Create an encrypted index
def create_encrypted_index(documents, paillier):
    index = {}
    for doc_id, doc in documents.items():
        for word in doc:
            
            # Use a fixed random 'r' value for the encryption to ensure consistency
            r = 42  # Consistent value of r for all words
            encrypted_word = paillier.encrypt(paillier.public_key, word, r)

            if encrypted_word not in index:
                index[encrypted_word] = []
            
            index[encrypted_word].append(doc_id)
    return index


# Search encrypted index
def search_encrypted_index(query, encrypted_index, paillier):
    
    # Use the same fixed 'r' for the search query
    r = 42  # Same consistent r for search query
    encrypted_query = paillier.encrypt(paillier.public_key, query, r)
    
    # Compare with precomputed encrypted words
    if encrypted_query in encrypted_index:
        return encrypted_index[encrypted_query]
    else:
        return []


paillier = Paillier(keysize=512)
pub_key, priv_key = paillier.public_key, paillier.private_key

num1 = 15
num2 = 25
cipher1 = paillier.encrypt(pub_key, num1)
cipher2 = paillier.encrypt(pub_key, num2)

ciphertext_sum = (cipher1 * cipher2) % (pub_key[0] * pub_key[0])
decrypted_sum = paillier.decrypt(priv_key, pub_key, ciphertext_sum)

print(f"Ciphertext of a: {cipher1}")
print(f"Ciphertext of b: {cipher2}")
print(f"Ciphertext of a + b: {ciphertext_sum}")
print(f"Decrypted product: {decrypted_sum}")
print(f"Expected product: {num1 + num2}")


# Scalar multiplication with 3
scalar = 3
cipher_scalar_mul = pow(cipher1, scalar, pub_key[0] ** 2)

# Decrypt the result of the multiplication
decrypted_mul = paillier.decrypt(priv_key, pub_key, cipher_scalar_mul)
print(f"Decrypted product: {decrypted_mul}, Expected: {num1 * scalar}")

documents = {
    "ID_1": [45, 30, 35],
    "ID_2": [50, 25, 30],
    "ID_3": [20, 25, 45],
}

encrypted_index = create_encrypted_index(documents, paillier)
search_query = 45
results = search_encrypted_index(search_query, encrypted_index, paillier)
print(f"Documents containing {search_query}: {results}")

import time

# Batch encrypt a list of numbers
def batch_encrypt(numbers, paillier):
    return [paillier.encrypt(pub_key, num) for num in numbers]

# Batch decrypt a list of encrypted numbers
def batch_decrypt(encrypted_numbers, paillier):
    return [paillier.decrypt(priv_key, pub_key, enc_num) for enc_num in encrypted_numbers]

# Measure performance
def measure_performance(numbers):
    # Encrypt
    start = time.time()
    encrypted_numbers = batch_encrypt(numbers, paillier)
    encryption_time = time.time() - start

    # Homomorphic addition (sum all ciphertexts)
    start = time.time()
    cipher_sum = encrypted_numbers[0]
    for cipher in encrypted_numbers[1:]:
        cipher_sum = (cipher_sum * cipher) % (pub_key[0] ** 2)
    homomorphic_time = time.time() - start

    # Decrypt
    start = time.time()
    decrypted_sum = paillier.decrypt(priv_key, pub_key, cipher_sum)
    decryption_time = time.time() - start

    return encryption_time, homomorphic_time, decryption_time

# Test with small and large numbers
numbers_small = [10, 20, 30]
numbers_large = [10000, 20000, 30000]

# Measure small
enc_time, hom_time, dec_time = measure_performance(numbers_small)
print(f"Small numbers -> Encryption: {enc_time}, Homomorphic: {hom_time}, Decryption: {dec_time}")

# Measure large
enc_time, hom_time, dec_time = measure_performance(numbers_large)
print(f"Large numbers -> Encryption: {enc_time}, Homomorphic: {hom_time}, Decryption: {dec_time}")
