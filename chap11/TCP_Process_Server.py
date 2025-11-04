import socket

table = {
    '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
    '9': 'nine', '10': 'ten'
}

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('0.0.0.0', 2500)
s.bind(address)
s.listen(1)
print("Waiting for connection...")

c_socket, c_addr = s.accept()
print("Connection from", c_addr)

while True:
    data = c_socket.recv(1024).decode()
    if not data:
        break

    try:
        resp = table[data]
    except KeyError:
        resp = "Try again"

    c_socket.send(resp.encode())

c_socket.close()
print("서버 종료")
