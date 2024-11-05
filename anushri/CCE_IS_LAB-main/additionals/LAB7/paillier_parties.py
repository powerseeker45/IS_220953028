from Crypto.Util import number
from Crypto.Random import random

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
        print(pub_key)
        n, _ = pub_key
        lambda_n, mu = priv_key
        u = pow(c, lambda_n, n * n)
        l = (u - 1) // n
        m = (l * mu) % n
        return m


# Simulate scenario where Alice and Bob share encrypted data

# Initialize ElGamal encryption system
paillier = Paillier()

# 1. Generate keys for both Alice and Bob
alice_public_key, alice_private_key = paillier.generate_keypair()
bob_public_key, bob_private_key = paillier.generate_keypair()


# 2. Alice encrypts her number (5) and Bob encrypts his number (7)
alice_number = 5
bob_number = 7

print("Alice's number:", alice_public_key)

# Encrypt using their respective public keys
alice_c = paillier.encrypt(alice_public_key, alice_number)
bob_c = paillier.encrypt(bob_public_key, bob_number)

# 3. Alice and Bob share encrypted data (c1, c2 values)

# 4. Perform homomorphic multiplication on encrypted values
# Alice multiplies her c1 and c2 with Bob's c1 and c2
combined_c = (alice_c* bob_c) % alice_public_key[0] 

# 5. Either Alice or Bob can now decrypt the result
# Alice decrypts the combined result using her private key
combined_result = paillier.decrypt(alice_private_key, alice_public_key, combined_c)

# Output the result
print("Homomorphic multiplication result (in bytes):", combined_result)
#print("Homomorphic multiplication result (as integer):", number.bytes_to_long(combined_result))
