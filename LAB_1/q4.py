#Hill cipher
import numpy as np
def encrypt(plaintext, key):
    # Convert plaintext to numerical values
    plaintext = plaintext.replace(" ","").upper()

    pt = [ord(char) - ord('A') for char in plaintext]

    if len(pt)%2 != 0:
        pt.append(ord('X')-ord('A'))
    pt=np.array(pt).reshape(-1,2)

    ct=(pt @ key)%26
    ct=''.join(chr(num+ ord('A')) for num in ct.flatten())

    return ct

def decrypt(ciphertext,key):
    # Convert ciphertext to numerical values
    ct = [ord(char) - ord('A') for char in ciphertext]
    ct=np.array(ct).reshape(-1,2)

    key_inv=np.linalg.inv(key)
    key_inv=key_inv%26


    pt=(ct @ key_inv)%26
    pt=''.join(chr(num+ ord('A')) for num in pt.flatten())

    return pt

def main():
    key = np.array([[3,3], [2,7]]) # key matrix
    message="We live in an insecure world"
    ciphertext=encrypt(message,key)
    print(ciphertext)

    plaintext=decrypt(ciphertext,key)

if __name__=='__main__':
    main()

    
    




