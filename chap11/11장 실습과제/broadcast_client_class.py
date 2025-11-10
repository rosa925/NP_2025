import socket

class BroadcastClient:
    def __init__(self, bcast_addr="<broadcast>", port=10000, bufsize=1024):
        self.bcast_addr = bcast_addr  # 예: "<broadcast>" 또는 "192.168.0.255"
        self.port = port
        self.bufsize = bufsize
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 브로드캐스트 옵션
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        # Windows에서 포트 재사용 도움 (선택)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def send_loop(self):
        try:
            while True:
                smsg = input("Broadcast Message (q to quit): ")
                if smsg.lower() == 'q':
                    break
                self.sock.sendto(smsg.encode('utf-8'), (self.bcast_addr, self.port))
                print(f"[BroadcastClient] Sent -> ({self.bcast_addr}, {self.port})")
        except KeyboardInterrupt:
            print("\n[BroadcastClient] Stopped.")
        finally:
            self.sock.close()

if __name__ == "__main__":
    # 필요 시 서브넷 브로드캐스트 주소로 변경: bcast_addr="192.168.0.255"
    client = BroadcastClient(bcast_addr="<broadcast>", port=10000)
    client.send_loop()
