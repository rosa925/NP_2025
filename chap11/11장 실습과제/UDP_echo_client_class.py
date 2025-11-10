import socket

class UDPClient:
    def __init__(self, server_host='172.31.141.150', port=5000, buffer_size=1024):
        self.server_host = server_host
        self.port = port
        self.buffer_size = buffer_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start(self):
        """서버와 메시지 송수신"""
        msg = "Hello UDP server"
        self.sock.sendto(msg.encode('utf-8'), (self.server_host, self.port))
        print(f"[UDPClient] Sent: {msg}")

        while True:
            data, addr = self.sock.recvfrom(self.buffer_size)
            print(f"[UDPClient] Server says: {data.decode('utf-8')}")
            msg = input("Sending message (q to quit): ")
            if msg.lower() == 'q':
                print("[UDPClient] Connection closed.")
                break
            self.sock.sendto(msg.encode('utf-8'), addr)

        self.sock.close()

if __name__ == "__main__":
    client = UDPClient(server_host='172.31.141.150', port=5000)
    client.start()
