# 예외처리를 한 TCP 클라이언트 프로그램
# 실행할 때 서버 주소와 포트를 지정한다.
# 지정하지 않으면 '127.0.0.1'과 2500 사용

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
