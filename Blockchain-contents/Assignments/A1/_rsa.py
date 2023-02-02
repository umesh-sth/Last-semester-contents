#Praceice asymmetric encryption - #18
#Importing library
import rsa
#Generating public and private keys with key length 512,
# where minimum keylength is 16
publicKey, privateKey = rsa.newkeys(512)
 # message to encrypt
message = "Hello Kathmandu University!"
#Encrypting string with public key
# encoding to byte string for the encryption
encryptMessage = rsa.encrypt(message.encode(), publicKey)
print("Original string: ", message)
print("Encrypted string: ", encryptMessage)
#Decrypting the message by private key 
decryptMessage = rsa.decrypt(encryptMessage, privateKey).decode()
print("decrypted string: ", decryptMessage)