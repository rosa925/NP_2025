import socket
import struct

class MulticastReceiver:
    def __init__(self, group_ip="224.0.0.255", port=5005, bufsize=1024):
        self.group_ip = group_ip
        self.port = port
        self.bufsize = bufsize

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        # 여러 프로세스/프로그램이 같은 포트를 바인드할 수 있게(환경에 따라 무시될 수 있음)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 모든 인터페이스에서 수신
        self.sock.bind(('', self.port))

        # 멀티캐스트 그룹 가입
        mreq = struct.pack("4sl", socket.inet_aton(self.group_ip), socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

        print(f"[MulticastReceiver] Ready to receive on group {self.group_ip}:{self.port}")

    def serve_forever(self, reply_text="ACK"):
        while True:
            data, addr = self.sock.recvfrom(self.bufsize)
            msg = data.decode('utf-8', errors='ignore')
            print(f"[RECV] '{msg}' from {addr}")
            # 발신자(유니캐스트)로 응답
            self.sock.sendto(reply_text.encode('utf-8'), addr)

    def close(self):
        try:
            mreq = struct.pack("4sl", socket.inet_aton(self.group_ip), socket.INADDR_ANY)
            self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_DROP_MEMBERSHIP, mreq)
        finally:
            self.sock.close()


if __name__ == "__main__":
    recv = MulticastReceiver(group_ip="224.0.0.255", port=5005)
    try:
        recv.serve_forever()
    finally:
        recv.close()
