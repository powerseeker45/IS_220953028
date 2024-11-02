#additive cipher key =20


def additive_cipher_enc(plainText,key):

	encryptedText=""
	for c in plainText:
		
		if (c.isupper()):
			encryptedText+=chr((c+key-64)%26 +65)
		elif (c.islower()):
			encryptedText+=chr((c+key-96)%26 +97)
		else:

			encryptedText+=c

	return encryptedText

def additive_cipher_dec(encryptedText,key):
	plainText=""

	for c in encryptedText:
		if (c.isupper()):
			encryptedText+=chr((c-key-64)%26 +65)
		elif (c.islower()):
			encryptedText+=chr((c-key-96)%26 +97)
		else:

			encryptedText+=c
	return plainText 



pt=input("enter plain text : ")
k= int(input("enter key : "))

enc=additive_cipher_enc(pt,k)

print("encrypted text is : "+enc)
print()

print("decrypting")
dec=additive_cipher_dec(enc,key)
print("decripted text is : "+dec)