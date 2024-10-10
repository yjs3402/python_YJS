from socket import *
from select import select
import sys

HOST = '127.0.0.1'
PORT = 2500
BUFSIZE = 1024
ADDR = (HOST, PORT)

clientSocket = socket(AF_INET, SOCK_STREAM)

# 서버와의 연결을 시도
try:
    clientSocket.connect(ADDR)
except Exception as e:
    print('채팅 서버(%s:%s)에 연결할 수 없습니다.' % ADDR)
    sys.exit()
print('채팅 서버(%s:%s)에 연결 되었습니다.' % ADDR)

def prompt():
    sys.stdout.write('<나>')
    sys.stdout.flush()

# 무한 루프를 시작
while True:
    try:
        #connection_list = [sys.stdin, clientSocket]
        connection_list = [clientSocket]

        read_socket, write_socket, error_socket = select(connection_list, [], [], 10)

        for sock in read_socket:
            if sock == clientSocket:
#                clientSocket.send('Hello Server'.encode())
                data = sock.recv(BUFSIZE)
                if not data:
                    print('채팅 서버(%s:%s)와의 연결이 끊어졌습니다.' % ADDR)
                    clientSocket.close()
                    sys.exit()
                else:
                    print('%s' % data.decode()) # 메세지 시간은 서버 시간을 따른다
                    prompt()
#            else:
#                message = sock.readline()
#                message = message.replace('\n', '')
#                clientSocket.send(message.encode())
#                prompt()
        message = sys.stdin.readline()
        message = message.replace('\n', '')
        clientSocket.send(message.encode())
        prompt()
    except KeyboardInterrupt:
        clientSocket.close()
        sys.exit()
                












                
