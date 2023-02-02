import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from keys import call_this

call_this()
HOST = '127.0.0.1'
PORT = 1234

ser_private_key = RSA.import_key(open('ser_private_key.pem').read())
ser_private_key = PKCS1_OAEP.new(ser_private_key)

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
        intro = cli_public_key.encrypt(intro)
        # print(intro)        
        connection.sendall(intro)
        while True:
            data = connection.recv(1024)
            data = ser_private_key.decrypt(data)
            data = data.decode("utf-8")
            if not data:
                print ('No data from client, Session terminated ')
                break

            print(" Client: " + str(data))
            data = input('  -> ')
            data = cli_public_key.encrypt(data.encode())
            connection.sendall(data)
        connection.close()
