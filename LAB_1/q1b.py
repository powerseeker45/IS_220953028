#q1b
def encrypt(text,s):
    result = ""

    if(s==0):
    	return text

    # traverse text
    for char in text:
        #char = text[i]

        # Encrypt uppercase characters

        if (char==' '):
        	result+=char

        elif (char.isupper()):
            result += chr(((ord(char) -65)*s) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr(((ord(char)- 97)*s) % 26 + 97)

    return result

def decrypt(text,s):
    result = ""

    if (s==0):
    	return text
    else:
    	s=pow(s,-1,26)

    for i in range(len(text)):
        char = text[i]

        if (char==' '):
        	result+=char


        elif (char.isupper()):
            result += chr(((ord(char) -65)*s) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr(((ord(char)- 97)*s) % 26 + 97)
    return result 

#check the above function
text = str(input("enter plaintext : "))
key = int(input("enter key : "))
cipher=encrypt(text,key)
print ("Text     : " + text)
print ("Shift 	 : " + str(key))
print ("Cipher	 : " + cipher)
print ("Decrypted: "+ decrypt(cipher,key))