from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

key = get_random_bytes(16)  # AES-128 requires a 16-byte key
cipher = AES.new(key, AES.MODE_ECB)

# Encrypt
plaintext = b'This is a secret message'
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# Decrypt
decipher = AES.new(key, AES.MODE_ECB)
decrypted_message = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("ECB Mode Decrypted:", decrypted_message)


key = get_random_bytes(16)
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CBC, iv)

# Encrypt
plaintext = b'This is a secret message'
ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

# Decrypt
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_message = unpad(decipher.decrypt(ciphertext), AES.block_size)

print("CBC Mode Decrypted:", decrypted_message)


key = get_random_bytes(16)
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_CFB, iv)

# Encrypt
plaintext = b'This is a secret message'
ciphertext = cipher.encrypt(plaintext)

# Decrypt
decipher = AES.new(key, AES.MODE_CFB, iv)
decrypted_message = decipher.decrypt(ciphertext)

print("CFB Mode Decrypted:", decrypted_message)


key = get_random_bytes(16)
iv = get_random_bytes(16)
cipher = AES.new(key, AES.MODE_OFB, iv)

# Encrypt
plaintext = b'This is a secret message'
ciphertext = cipher.encrypt(plaintext)

# Decrypt
decipher = AES.new(key, AES.MODE_OFB, iv)
decrypted_message = decipher.decrypt(ciphertext)

print("OFB Mode Decrypted:", decrypted_message)


key = get_random_bytes(16)
nonce = get_random_bytes(8)  # 64-bit nonce for CTR mode
cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)

# Encrypt
plaintext = b'This is a secret message'
ciphertext = cipher.encrypt(plaintext)

# Decrypt
decipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
decrypted_message = decipher.decrypt(ciphertext)

print("CTR Mode Decrypted:", decrypted_message)

key = get_random_bytes(16)
nonce = get_random_bytes(12)  # Recommended 96-bit nonce for GCM
cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

# Encrypt
plaintext = b'This is a secret message'
ciphertext, tag = cipher.encrypt_and_digest(plaintext)

# Decrypt
decipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
decrypted_message = decipher.decrypt_and_verify(ciphertext, tag)

print("GCM Mode Decrypted:", decrypted_message)
