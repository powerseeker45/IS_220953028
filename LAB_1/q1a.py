#q1i

def encrypt(text,s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters

        if (char==' '):
        	result+=char

        elif (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

def decrypt(text,s):
    result = ""

    
    for i in range(len(text)):
        char = text[i]

        if (char==' '):
        	result+=char


        elif (char.isupper()):
            result += chr((ord(char) - s-65) % 26 + 65)

        
        else:
            result += chr((ord(char) -s - 97) % 26 + 97)

    return result

#check the above function
text = str(input("enter plaintext : "))
key = int(input("enter key : "))
cipher=encrypt(text,key)
print ("Text     : " + text)
print ("Shift 	 : " + str(key))
print ("Cipher	 : " + cipher)
print ("Decrypted: "+ decrypt(cipher,key))


