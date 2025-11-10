import socket

class TimeClient:
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        """서버에 연결"""
        try:
            self.sock.connect((self.host, self.port))
            print(f"[TimeClient] Connected to {self.host}:{self.port}")
        except Exception as e:
            print("[TimeClient] Connection failed:", e)

    def receive_time(self):
        """서버로부터 시간 데이터를 수신"""
        try:
            data = self.sock.recv(1024)
            print("현재 시각:", data.decode('utf-8'))
        except Exception as e:
            print("[TimeClient] Error receiving data:", e)

    def close(self):
        """소켓 종료"""
        self.sock.close()
        print("[TimeClient] Connection closed.")

if __name__ == "__main__":
    client = TimeClient(host='172.31.141.150', port=5000)
    client.connect()
    client.receive_time()
    client.close()
