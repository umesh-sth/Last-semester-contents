import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from keys import call_this

# function that creates keys for server and client
call_this()

# defining host and port
HOST = '127.0.0.1'
PORT = 1234

# importing and defining cipher/private key for server
ser_private_key = RSA.import_key(open('ser_private_key.pem').read())
ser_private_key = PKCS1_OAEP.new(ser_private_key)

# importing and defingin public key for client
cli_public_key = RSA.import_key(open('cli_public_key.pem').read())
cli_public_key = PKCS1_OAEP.new(cli_public_key)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Server:
    Server.bind((HOST, PORT))
    Server.listen()
    print (f'Started listening at IP :{HOST}  Port :{PORT}')
    print ('Waiting for a connection ....')
    connection, address = Server.accept()
    with connection:
        print(f'Connection has been established with {address}')
        intro = b'hello from Server!'
        # encrypting the text that is to be send to client from server, using public key of client
        intro = cli_public_key.encrypt(intro)
        # sending message to client
        connection.sendall(intro)
        while True:
            # receiving data from connected client
            data = connection.recv(1024)
            # decrypting the message send by client using private key of server
            data = ser_private_key.decrypt(data)
            # decoding the decrypted cipher into plain text
            data = data.decode("utf-8")
            if not data:
                print ('No data from client, Session terminated ')
                break

            print(" Client: " + str(data))
            data = input('  -> ')
            # encrypting message using client public key
            data = cli_public_key.encrypt(data.encode())
            connection.sendall(data)
        # close connection whenever no client is connected
        connection.close()
