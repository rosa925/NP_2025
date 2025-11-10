import socket
port = 5000
BUFFER = 1024

sock = socket.socket(socket.AF_INET, socket.SOCKET_DGRAM)
sock.bind(('', port))
print("수신 대기 중")

while True:
    data, addr = sock.recvfrom(BUFFER)
    print("Received message: ", data.decode())
    print(addr)
    sock.sendto(data, addr)