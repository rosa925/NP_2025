import socket

class NumberClient:
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host   # 서버 IP 주소 (예: '172.31.141.150')
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.sock.connect((self.host, self.port))
            print(f"[NumberClient] Connected to {self.host}:{self.port}")
        except Exception as e:
            print("[NumberClient] Connection failed:", e)
            exit(1)

    def start(self):
        try:
            while True:
                msg = input("정수 입력 (종료: quit): ")
                self.sock.sendall((msg + "\n").encode("utf-8"))

                if msg.lower() == "quit":
                    data = self.sock.recv(1024)
                    if not data:
                        break
                    print("서버 응답:", data.decode("utf-8").strip())
                    break

                data = self.sock.recv(1024)
                if not data:
                    print("[NumberClient] 서버에서 연결이 종료되었습니다.")
                    break

                print("서버 응답:", data.decode("utf-8").strip())

        except Exception as e:
            print("[NumberClient] Error:", e)

        finally:
            self.sock.close()
            print("[NumberClient] Connection closed.")


if __name__ == "__main__":
    # 서버가 Ubuntu(WLS)라면 host 값을 여기서 수정
    client = NumberClient(host='127.0.0.1', port=5000)
    client.connect()
    client.start()
