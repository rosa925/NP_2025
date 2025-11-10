import socket

class BroadcastServer:
    def __init__(self, host='', port=10000, bufsize=1024):
        self.host = host            # '' = 모든 인터페이스
        self.port = port
        self.bufsize = bufsize
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 동일 포트 재바인드 허용
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        print(f"[BroadcastServer] Listening on {self.host or '0.0.0.0'}:{self.port}")

    def serve_forever(self):
        while True:
            try:
                msg, addr = self.sock.recvfrom(self.bufsize)
                text = msg.decode('utf-8', errors='ignore')
                print(f"[BroadcastServer] From {addr}: {text}")
            except KeyboardInterrupt:
                print("\n[BroadcastServer] Stopped.")
                break
            except Exception as e:
                print("[BroadcastServer] Error:", e)

        self.sock.close()

if __name__ == "__main__":
    server = BroadcastServer(port=10000)
    server.serve_forever()
