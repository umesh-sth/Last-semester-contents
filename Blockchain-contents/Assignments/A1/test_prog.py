from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import unittest
from keys import call_this

call_this()
ser_private_key = RSA.import_key(open('ser_private_key.pem').read())
ser_private_key = PKCS1_OAEP.new(ser_private_key)

cli_public_key = RSA.import_key(open('cli_public_key.pem').read())
cli_public_key = PKCS1_OAEP.new(cli_public_key)

ser_public_key = RSA.import_key(open('ser_public_key.pem').read())
ser_public_key = PKCS1_OAEP.new(ser_public_key)

cli_private_key = RSA.import_key(open('cli_private_key.pem').read())
cli_private_key = PKCS1_OAEP.new(cli_private_key)

client_msg = "hello, server"
server_msg = "hello, client"


class TestCrypto(unittest.TestCase):

    def test_encryption_from_server(self):
        self.ciphertext = ser_public_key.encrypt(client_msg.encode())
        self.plaintext  = ser_private_key.decrypt(self.ciphertext)
        self.plaintext = self.plaintext.decode("utf-8")
        self.assertEqual(self.plaintext, client_msg)
    
    def test_encryption_from_client(self):
        self.ciphertext = cli_public_key.encrypt(server_msg.encode())
        self.plaintext  = cli_private_key.decrypt(self.ciphertext)
        self.plaintext = self.plaintext.decode("utf-8")
        self.assertEqual(self.plaintext, server_msg)
        
        

if __name__ == '__main__':
    unittest.main()


    