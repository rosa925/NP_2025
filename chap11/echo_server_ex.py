from socket import *

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('0.0.0.0', port))
sock.listen(1)
print(f"[ECHO SERVER] Listening on port {port}...")

conn, (remotehost, remoteport) = sock.accept()
print('Connected by', remotehost, remoteport)

while True:
    try:
        data = conn.recv(BUFSIZE)   # 수신 시도
    except Exception as e:
        print("❌ 수신 중 예외 발생:", e)
        conn.close()
        break

    if not data:
        print("클라이언트 연결 종료")
        conn.close()
        break

    try:
        print("Received message:", data.decode())
        conn.send(data)              # 에코 응답
    except Exception as e:
        print("❌ 송신 중 예외 발생:", e)
        conn.close()
        break

print("서버 종료")
