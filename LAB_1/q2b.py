#q2b
#Autokey cipher with key = 7

def encrypt(text,keyword):
    result = ""

    j=0

    keyword+=text
    for i in range(len(text)):
        char = text[i]
        key = keyword[j]


        if (char==' '):
            result+=char

        elif (char.isupper()):
            result += chr(((ord(char) -65)+ord(key)) % 26 + 65)

        else:
            result += chr((((ord(char)- 97))+ord(key)) % 26 + 97)

        j=(j+1)%len(keyword)
      
    return result

def decrypt(text,keyword):
    result = ""

    j=0


    keyword=keyword+text
    for i in range(len(text)):
        char = text[i]
        key = keyword[j]


        if (char==' '):
            result+=char

        elif (char.isupper()):
            result += chr(((ord(char) -65)-ord(key)) % 26 + 65)

        else:
            result += chr((((ord(char)- 97))-ord(key)) % 26 + 97)

        j=(j+1)%len(keyword)
        


    return result 

#check the above function
text = str(input("enter plaintext : "))
key = str(input("enter key : "))
cipher=encrypt(text,key)
print ("Text     : " + text)
print ("key      : " + key)
print ("Cipher   : " + cipher)
print ("Decrypted: "+ decrypt(cipher,key))