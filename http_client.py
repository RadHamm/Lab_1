from socket import * 
import ssl
server_name = 'gaia.cs.umass.edu' 
server_port = 443
# 1. Create a TCP socket (IPv4) 
# Hint: Use AF_INET for IPv4 and SOCK_STREAM for TCP 
client_socket = socket(AF_INET, SOCK_STREAM) 
# 1.5. Wrap the socket with SSL
context = ssl.create_default_context()
secure_socket = context.wrap_socket(client_socket, server_hostname=server_name)
# 2. Connect to the server 
secure_socket.connect((server_name, server_port)) 
# 3. Prepare the HTTP request 
# Critical: HTTP requires carriage return & new line (\r\n) at the end of headers 
# The double \r\n\r\n indicates the end of the header section. 
request = "GET /kurose_ross/interactive/index.php HTTP/1.1\r\nHost: gaia.cs.umass.edu\r\n\r\n" 
# 4. Send the request 
# We must encode the string into bytes before sending 
secure_socket.send(request.encode()) 
# 5. Receive the response 
# We read up to 4096 bytes 
response = secure_socket.recv(4096) 
# 6. Decode and print the result 
print(response.decode()) 
# 7. Close the connnection
secure_socket.close()