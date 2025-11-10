import socket
import time

class TimeServer:
    def __init__(self, host='0.0.0.0', port=5000):
        self.host = host
        self.port = port
        # TCP 소켓 생성S
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        """서버 실행 메서드"""
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        print(f"[TimeServer] Listening on {self.host}:{self.port}")

        while True:
            client, addr = self.sock.accept()
            print(f"[TimeServer] Connection requested from {addr}")
            self.handle_client(client)

    def handle_client(self, client_socket):
        """클라이언트 요청 처리"""
        try:
            current_time = time.ctime(time.time())
            client_socket.send(current_time.encode('utf-8'))
            print(f"[TimeServer] Sent time: {current_time}")
        except Exception as e:
            print("[TimeServer] Error:", e)
        finally:
            client_socket.close()

if __name__ == "__main__":
    server = TimeServer()
    server.start()
