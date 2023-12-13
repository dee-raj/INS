# SSL server side

# https://www.cryptool.org/en/cto/openssl or search cryptool openssl
# in cmd of website type  openssl req -x509 -sha256 -nodes -newkey rsa:2048 -keyout localhost.key -out localhost.crt -days 365
# go down click files and download all three files and save in code directory

import socket
import ssl
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 4423))
server_socket.listen(5)
certfile = 'localhost.crt'
keyfile = 'localhost.key'
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile=certfile, keyfile=keyfile)
print("Server is listening on port 4423...")
true = True
while true:
   client_socket, client_address = server_socket.accept()
   ssl_client_socket = context.wrap_socket(client_socket, server_side=True)
   try:
      data = ssl_client_socket.recv(1024)
      if data:
         print("Received:", data.decode())
         ssl_client_socket.send(b"Hello, client!")
   except ssl.SSLError as e:
      print("SSL Error:", e)
   finally:
      ssl_client_socket.close()



"""
OUTPUT:-
PS C:\Users\students\Desktop\INS__> python .\sslserver.py
Server is listening on port 4423...
Received: Hello, server!
"""




# SSL clint side
# https://www.cryptool.org/en/cto/openssl or search cryptool openssl
# in cmd of website type  openssl req -x509 -sha256 -nodes -newkey rsa:2048 -keyout localhost.key -out localhost.crt -days 365
# go down click files and download all three files 


import socket
import ssl
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = '127.0.0.1'
server_port = 4423
client_socket.connect((server_ip, server_port))
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
ssl_client_socket = context.wrap_socket(client_socket, server_hostname=server_ip)
try:
   ssl_client_socket.send(b"Hello, server!")
   response = ssl_client_socket.recv(1024)
   print("Server response:", response.decode())
except ssl.SSLError as e:
   print("SSL Error:", e)
finally:
   ssl_client_socket.close()


# """
# OUTPUT:-
# PS C:\Users\students\Desktop\INS__> python .\sslclient.py
# Server response: Hello, client!
# """