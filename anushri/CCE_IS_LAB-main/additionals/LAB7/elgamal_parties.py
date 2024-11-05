from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
from Crypto.Random import random

class Elgamal:
    def generate_keys(self):
        # Generate large prime p
        p = getPrime(2048)  
        # Generator g
        g = random.randint(2, p - 1)  
        # Private key x
        x = random.randint(2, p - 2)  
        # Public key h = g^x mod p
        h = pow(g, x, p)  
        # Public key is (p, g, h) and private key is x
        return (p, g, h), x

    def elgamal_encrypt(self, public_key, message):
        p, g, h = public_key
        # Convert message to long (for proper encryption of numbers)
        m = bytes_to_long(message)
        # Random value k
        k = random.randint(2, p - 2)  
        # Compute c1 = g^k mod p
        c1 = pow(g, k, p)  
        # Compute c2 = m * h^k mod p
        c2 = (m * pow(h, k, p)) % p  
        return c1, c2

    def elgamal_decrypt(self, private_key, p, c1, c2):
        x = private_key
        # Compute shared secret s = c1^x mod p
        s = pow(c1, x, p) 
        # Compute modular inverse of s
        s_inv = inverse(s, p) 
        # Recover the message m = c2 * s_inv mod p
        m = (c2 * s_inv) % p 
        return long_to_bytes(m)

# Simulate scenario where Alice and Bob share encrypted data

# Initialize ElGamal encryption system
elgamal = Elgamal()

# 1. Generate keys for both Alice and Bob
alice_public_key, alice_private_key = elgamal.generate_keys()
bob_public_key, bob_private_key = elgamal.generate_keys()

# 2. Alice encrypts her number (5) and Bob encrypts his number (7)
alice_number = b'5'
bob_number = b'7'

# Encrypt using their respective public keys
alice_c1, alice_c2 = elgamal.elgamal_encrypt(alice_public_key, alice_number)
bob_c1, bob_c2 = elgamal.elgamal_encrypt(bob_public_key, bob_number)

# 3. Alice and Bob share encrypted data (c1, c2 values)

# 4. Perform homomorphic multiplication on encrypted values
# Alice multiplies her c1 and c2 with Bob's c1 and c2
combined_c1 = (alice_c1 * bob_c1) % alice_public_key[0]  # Mod p from Alice's public key
combined_c2 = (alice_c2 * bob_c2) % alice_public_key[0]

# 5. Either Alice or Bob can now decrypt the result
# Alice decrypts the combined result using her private key
combined_result = elgamal.elgamal_decrypt(alice_private_key, alice_public_key[0], combined_c1, combined_c2)

# Output the result
print("Homomorphic multiplication result (in bytes):", combined_result)
print("Homomorphic multiplication result (as integer):", bytes_to_long(combined_result))
