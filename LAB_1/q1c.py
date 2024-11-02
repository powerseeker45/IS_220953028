#q1c
def encrypt(text,s,b):
    result = ""

    if(s==0):
    	return text

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters

        if (char==' '):
        	result+=char

        elif (char.isupper()):
            result += chr((((ord(char) -65)*s)+b) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((((ord(char)- 97)*s)+b) % 26 + 97)

    return result

def decrypt(text,s,b):
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
            result += chr(((ord(char) -65-b)*s) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr(((ord(char)- 97 -b)*s) % 26 + 97)
    return result 

#check the above function
text = str(input("enter plaintext : "))
a = int(input("enter a : "))
b = int(input("enter b :"))
cipher=encrypt(text,a,b)
print ("Text     : " + text)
print ("key 	 : " + str(a)+"x + "+str(b))
print ("Cipher	 : " + cipher)
print ("Decrypted: "+ decrypt(cipher,a,b))