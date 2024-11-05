from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Step 1: Generate RSA keys (for digital signature)
def generate_rsa_keypair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Step 2: Sign the message using RSA
def sign_message(private_key, message):
    key = RSA.import_key(private_key)
    hash_message = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(hash_message)
    return signature

# Step 3: Verify the signature using RSA
def verify_signature(public_key, message, signature):
    key = RSA.import_key(public_key)
    hash_message = SHA256.new(message)
    try:
        pkcs1_15.new(key).verify(hash_message, signature)
        print("Signature is valid.")
        return True
    except (ValueError, TypeError):
        print("Signature is invalid.")
        return False

# Step 4: Encrypt the message using AES
def aes_encrypt(message, key):
    cipher_aes = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher_aes.encrypt(pad(message, AES.block_size))
    return ciphertext, cipher_aes.iv

# Step 5: Decrypt the message using AES
def aes_decrypt(ciphertext, key, iv):
    cipher_aes = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher_aes.decrypt(ciphertext), AES.block_size)
    return decrypted_message

# Step 6: Example usage
def main():
    # Message to be sent
    message = b"Sensitive information that needs to be encrypted and signed."

    # 1. Generate RSA key pair for digital signature
    private_key, public_key = generate_rsa_keypair()
    
    # 2. Sign the message
    signature = sign_message(private_key, message)
    print(f"Digital Signature: {signature}")

    # 3. AES Encryption (Symmetric Encryption)
    aes_key = get_random_bytes(16)  # 128-bit AES key
    ciphertext, iv = aes_encrypt(message, aes_key)
    print(f"Encrypted Message: {ciphertext}")

    # 4. Send (ciphertext + signature) to the recipient...

    # 5. Receiver verifies the signature
    is_signature_valid = verify_signature(public_key, message, signature)
    
    # 6. If valid, decrypt the message
    if is_signature_valid:
        decrypted_message = aes_decrypt(ciphertext, aes_key, iv)
        print(f"Decrypted Message: {decrypted_message.decode()}")

if __name__ == "__main__":
    main()
