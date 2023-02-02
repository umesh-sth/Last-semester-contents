import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

HOST = '127.0.0.1'   # Server's hostname or IP address
PORT = 1234          # Port used by the server

# importing public key of server
ser_public_key = RSA.import_key(open('ser_public_key.pem').read())
ser_public_key = PKCS1_OAEP.new(ser_public_key)

# importing private key of client
cli_private_key = RSA.import_key(open('cli_private_key.pem').read())
cli_private_key = PKCS1_OAEP.new(cli_private_key)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as Client:
    # connect to host using the port
    Client.connect((HOST, PORT))
    
    # receive data form the server
    data = Client.recv(1024)
    # decrypt msg send from server usign the client private key
    data = cli_private_key.decrypt(data)
    # decode the decrypted data using utf-8
    data =data.decode("utf-8")
    print('Server : '+data)
    msg = input('  -> ')
    while msg.lower().strip() != 'bye':
        # encrypting encoded msg usign server public key
        msg = ser_public_key.encrypt(msg.encode())
        Client.sendall(msg)
        # receicing msg from server
        data = Client.recv(1024)
        ## decrypt msg send from server usign the client private key
        data = cli_private_key.decrypt(data)
        data = data.decode("utf-8")
        print(' Server : '+data)
        msg = input(' -> ')
        
    # encrypting encoded msg usign server public key
    msg = ser_public_key.encrypt(msg.encode())    
    Client.sendall(msg)
    Client.close()      