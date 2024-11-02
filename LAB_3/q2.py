import tinyec.ec as ec
import tinyec.registry as reg
import secrets

# Get the curve
curve = reg.get_curve("brainpoolP256r1")

# Key generation
private_key = secrets.randbelow(curve.field.n)
public_key = private_key * curve.g

# Function to encrypt the message
def ecc_encrypt(msg, pub_key, curve):
    msg_point = ec.Point(curve, int.from_bytes(msg.encode(), 'big'), 0)
    k = secrets.randbelow(curve.field.n)
    C1 = k * curve.g
    C2 = msg_point + k * pub_key
    return (C1, C2)

# Function to decrypt the ciphertext
def ecc_decrypt(ciphertext, priv_key, curve):
    C1, C2 = ciphertext
    decrypted_point = C2 - priv_key * C1
    decrypted_msg = int.to_bytes(decrypted_point.x, length=(decrypted_point.x.bit_length() + 7) // 8, byteorder='big')
    return decrypted_msg.decode()

# Message to encrypt
message = "Secure Transactions"

# Encrypt the message
ciphertext = ecc_encrypt(message, public_key, curve)
print("Encrypted Message:", ciphertext)

# Decrypt the message
decrypted_message = ecc_decrypt(ciphertext, private_key, curve)
print("Decrypted Message:", decrypted_message)
