import socket
import threading

SERVER_HOST = "172.31.141.150"  # 서버 IP
SERVER_PORT = 2500              # 서버 포트 (서버 코드와 반드시 동일해야 함)

def recv_thread(sock: socket.socket):
    """서버에서 오는 메시지를 계속 수신해서 출력하는 스레드"""
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("[알림] 서버와의 연결이 종료되었습니다.")
                break
            print("\n[수신] ", data.decode('utf-8').strip())
        except Exception as e:
            print("[수신 스레드 오류]", e)
            break
    sock.close()

def main():
    # 서버에 TCP 연결
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((SERVER_HOST, SERVER_PORT))
        print(f"[연결 성공] 서버 {SERVER_HOST}:{SERVER_PORT}")
    except Exception as e:
        print("[연결 실패]", e)
        return

    # 수신 전용 스레드 시작
    t = threading.Thread(target=recv_thread, args=(sock,))
    t.daemon = True
    t.start()

    # 메인 스레드는 메시지 입력 후 전송
    try:
        while True:
            msg = input("메시지 입력 (quit 입력 시 종료): ")
            if not msg:
                continue

            # 메시지 끝에 개행 문자 추가 → 자바 서버의 readLine()과 맞추기
            send_data = (msg + "\n").encode('utf-8')

            if msg.lower() == "quit":
                sock.sendall(send_data)
                break

            sock.sendall(send_data)

    except KeyboardInterrupt:
        print("\n[클라이언트] 사용자가 종료함")
    finally:
        sock.close()
        print("[클라이언트 종료]")

if __name__ == "__main__":
    main()
