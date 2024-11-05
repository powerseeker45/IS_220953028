from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


key = get_random_bytes(8)  # DES requires a 8-byte key
cipher = DES.new(key, DES.MODE_ECB)

# Encrypt
plaintext = b"This is a secret message"
ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))

# Decrypt
decipher = DES.new(key, DES.MODE_ECB)
decrypted_message = unpad(decipher.decrypt(ciphertext), DES.block_size)

print("ECB Mode Decrypted:", decrypted_message)


key = get_random_bytes(8)  # DES requires an 8-byte key
iv = get_random_bytes(8)  # IV is also 8 bytes for DES
cipher = DES.new(key, DES.MODE_CBC, iv)

# Encrypt
plaintext = b"This is a secret message"
ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))

# Decrypt
decipher = DES.new(key, DES.MODE_CBC, iv)
decrypted_message = unpad(decipher.decrypt(ciphertext), DES.block_size)

print("CBC Mode Decrypted:", decrypted_message)


key = get_random_bytes(8)
iv = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_CFB, iv)

# Encrypt
plaintext = b"This is a secret message"
ciphertext = cipher.encrypt(plaintext)

# Decrypt
decipher = DES.new(key, DES.MODE_CFB, iv)
decrypted_message = decipher.decrypt(ciphertext)

print("CFB Mode Decrypted:", decrypted_message)


key = get_random_bytes(8)
iv = get_random_bytes(8)
cipher = DES.new(key, DES.MODE_OFB, iv)

# Encrypt
plaintext = b"This is a secret message"
ciphertext = cipher.encrypt(plaintext)

# Decrypt
decipher = DES.new(key, DES.MODE_OFB, iv)
decrypted_message = decipher.decrypt(ciphertext)

print("OFB Mode Decrypted:", decrypted_message)


from Crypto.Util import Counter

key = get_random_bytes(8)
nonce = get_random_bytes(4)  # 32-bit nonce for DES-CTR
ctr = Counter.new(32, prefix=nonce)  # Create a counter for DES CTR

cipher = DES.new(key, DES.MODE_CTR, counter=ctr)

# Encrypt
plaintext = b"This is a secret message"
ciphertext = cipher.encrypt(plaintext)

# Decrypt
ctr = Counter.new(32, prefix=nonce)
decipher = DES.new(key, DES.MODE_CTR, counter=ctr)
decrypted_message = decipher.decrypt(ciphertext)

print("CTR Mode Decrypted:", decrypted_message)


#########TRIPLE DES


from Crypto.Cipher import DES3

key = DES3.adjust_key_parity(get_random_bytes(24))  # Triple DES requires a 24-byte key
iv = get_random_bytes(8)  # IV is still 8 bytes
cipher = DES3.new(key, DES3.MODE_CBC, iv)

# Encrypt
plaintext = b"This is a secret message"
ciphertext = cipher.encrypt(pad(plaintext, DES3.block_size))

# Decrypt
decipher = DES3.new(key, DES3.MODE_CBC, iv)
decrypted_message = unpad(decipher.decrypt(ciphertext), DES3.block_size)

print("3DES Mode Decrypted:", decrypted_message)
