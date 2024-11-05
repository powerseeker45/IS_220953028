#Implement ElGamal encryption and demonstrate homomorphic multiplication on encrypted messages. (ElGamal supports multiplication but not homomorphic addition.) 
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

# Messages to be encrypted (as bytes)
a = b'5'
b = b'7'

elgamal = Elgamal()
# Generate public and private keys
public_key, private_key = elgamal.generate_keys()

# Encrypt the messages a and b
c1_a, c2_a = elgamal.elgamal_encrypt(public_key, a)
c1_b, c2_b = elgamal.elgamal_encrypt(public_key, b)

# Perform homomorphic multiplication on encrypted messages
c1_mul = (c1_a * c1_b) % public_key[0]  # Multiply c1 values
c2_mul = (c2_a * c2_b) % public_key[0]  # Multiply c2 values

# Decrypt the result of the multiplication
result = elgamal.elgamal_decrypt(private_key, public_key[0], c1_mul, c2_mul)

# Print the result
print("Homomorphic multiplication result (in bytes):", result)
print("Homomorphic multiplication result (as integer):", bytes_to_long(result))
