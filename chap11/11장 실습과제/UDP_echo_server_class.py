import socket

class UDPServer:
    def __init__(self, host='0.0.0.0', port=5000, buffer_size=1024):
        self.host = host
        self.port = port
        self.buffer_size = buffer_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.host, self.port))
        print(f"[UDPServer] Listening on {self.host}:{self.port}")

    def start(self):
        """클라이언트 메시지 수신 및 응답"""
        while True:
            data, addr = self.sock.recvfrom(self.buffer_size)
            print(f"[UDPServer] Received from {addr}: {data.decode('utf-8')}")
            self.sock.sendto(data, addr)
            print(f"[UDPServer] Echoed message to {addr}")

if __name__ == "__main__":
    server = UDPServer()
    server.start()
