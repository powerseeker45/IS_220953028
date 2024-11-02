def generate_playfair_matrix(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x))).replace('J', 'I')
    matrix = [char for char in key if char.isalpha()]
    matrix += [char for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ' if char not in matrix]
    return matrix

def format_text(text, pairwise=True):
    text = text.replace('J', 'I').replace(' ', '').upper()
    if pairwise:
        formatted = []
        i = 0
        while i < len(text):
            if i + 1 < len(text) and text[i] == text[i + 1]:
                formatted.append(text[i] + 'X')
                i += 1
            else:
                formatted.append(text[i] + (text[i + 1] if i + 1 < len(text) else 'X'))
                i += 2
        return formatted
    return text

def playfair_cipher(key, text, decrypt=False):
    matrix = generate_playfair_matrix(key)
    pos = {matrix[i]: (i // 5, i % 5) for i in range(25)}
    formatted_text = format_text(text)
    
    def transform_pair(a, b):
        row1, col1 = pos[a]
        row2, col2 = pos[b]
        if row1 == row2:
            return matrix[row1 * 5 + (col1 + (1 if not decrypt else -1)) % 5] + matrix[row2 * 5 + (col2 + (1 if not decrypt else -1)) % 5]
        elif col1 == col2:
            return matrix[((row1 + (1 if not decrypt else -1)) % 5) * 5 + col1] + matrix[((row2 + (1 if not decrypt else -1)) % 5) * 5 + col2]
        else:
            return matrix[row1 * 5 + col2] + matrix[row2 * 5 + col1]
    
    result = ''.join(transform_pair(pair[0], pair[1]) for pair in formatted_text)
    return result

# Input from user
key = input("Enter the key for Playfair cipher: ").upper().replace('J', 'I')
message = input("Enter the message to encrypt: ")

# Encryption
cipher_text = playfair_cipher(key, message, decrypt=False)
print("Encrypted Text:", cipher_text)

# Decryption
decrypted_text = playfair_cipher(key, cipher_text, decrypt=True)
print("Decrypted Text:", decrypted_text)
