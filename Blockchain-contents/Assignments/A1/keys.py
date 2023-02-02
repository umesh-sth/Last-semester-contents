from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def call_this():
    # generating keys for client and server
    new_key1 = RSA.generate(1024)
    new_key2 = RSA.generate(1024)

    # generating keys for server
    ser_private_key = new_key1.exportKey("PEM")
    ser_public_key = new_key1.publickey().exportKey("PEM")

    # generating keys for client
    cli_private_key = new_key2.exportKey("PEM")
    cli_public_key = new_key2.publickey().exportKey("PEM")

    # storing private key for server
    fd = open("ser_private_key.pem", "wb")
    fd.write(ser_private_key)
    fd.close()

    # storing public key for server
    fd = open("ser_public_key.pem", "wb")
    fd.write(ser_public_key)
    fd.close()

    # storing private key for client
    fd = open("cli_private_key.pem", "wb")
    fd.write(cli_private_key)
    fd.close()

    # storing public key for client
    fd = open("cli_public_key.pem", "wb")
    fd.write(cli_public_key)
    fd.close()

# message = b'hello'


# key = RSA.import_key(open('cli_public_key.pem').read())
# cipher = PKCS1_OAEP.new(key)
# ciphertext = cipher.encrypt(message)
# print(ciphertext)
# print("\n\n")



# key = RSA.import_key(open('cli_private_key.pem').read())
# cipher = PKCS1_OAEP.new(key)
# plaintext = cipher.decrypt(ciphertext)
# print (plaintext.decode("utf-8"))