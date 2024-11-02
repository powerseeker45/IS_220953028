# RSA encryption function
def rsa_encrypt(message, n, e):
    # Convert message to numerical representation
    message_numbers = [ord(char) for char in message]
    
    # Encrypt the message using the public key (n, e)
    ciphertext_numbers = [(m ** e) % n for m in message_numbers]
    
    return ciphertext_numbers

# RSA decryption function
def rsa_decrypt(ciphertext, n, d):
    # Decrypt the message using the private key (n, d)
    decrypted_numbers = [(c ** d) % n for c in ciphertext]
    
    # Convert the decrypted numbers back to the original message
    decrypted_message = ''.join(chr(num) for num in decrypted_numbers)
    
    return decrypted_message

# Given RSA parameters
n = 3233
e = 17
d = 2753

# Ask user for the message to encrypt
message = input("Enter the message to encrypt: ")

# Encrypt the message
ciphertext = rsa_encrypt(message, n, e)
print("Encrypted Message (Ciphertext):", ciphertext)

# Decrypt the message
decrypted_message = rsa_decrypt(ciphertext, n, d)
print("Decrypted Message:", decrypted_message)
