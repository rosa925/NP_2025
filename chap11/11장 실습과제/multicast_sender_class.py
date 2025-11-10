import socket
import struct

class MulticastSender:
    def __init__(self, group_ip="224.0.0.255", port=5005, ttl=2, timeout=0.5):
        self.group_ip = group_ip
        self.port = port
        self.addr = (group_ip, port)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(timeout)

        # 멀티캐스트 TTL 설정 (홉 수)
        ttl_bytes = struct.pack('b', ttl)  # == struct.pack('@b', ttl)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl_bytes)

    def send_and_collect_replies(self, message: str, bufsize: int = 1024):
        """그룹으로 메시지를 전송하고, 타임아웃까지 도착한 응답을 모두 수집"""
        self.sock.sendto(message.encode('utf-8'), self.addr)
        replies = []
        while True:
            try:
                data, src = self.sock.recvfrom(bufsize)
                replies.append((src, data.decode('utf-8', errors='ignore')))
            except socket.timeout:
                break
        return replies

    def close(self):
        self.sock.close()


if __name__ == "__main__":
    sender = MulticastSender(group_ip="224.0.0.255", port=5005, ttl=2, timeout=0.5)
    try:
        while True:
            msg = input("Your message (q to quit): ")
            if msg.lower() == 'q':
                break
            results = sender.send_and_collect_replies(msg)
            for (src, text) in results:
                print(f"[REPLY] from {src}: {text}")
    finally:
        sender.close()
