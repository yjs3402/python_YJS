# -*- coding: utf8 -*-
import socket
import sys
from select import select
import datetime
import json

class OverlappedError(Exception):
	def __init__(self):
		super().__init__("\n※ 이미 사용중인 닉네임입니다. 다시 입력해주세요.\n")	

class ChatRoom(object):
	global connectionStatus
	
	def find_conn(self, connection_dict, nick_val):
		return next(conn for conn, nick in connection_dict.items() if nick_val == nick)
	
	def find_nick(self, connection_dict, conn_val):
		return next(nick for conn, nick in connection_dict.items() if conn_val == conn)

	def find_room_num(self, connection_status, conn_val):
		return next(room_num for room_num, connection_dict in connection_status.items() if conn_val in connection_dict)

	def manage_client(self, conn, data):
		self.nickname = data['client_nick']
		self.room_num = data['room_num']
		# 클라이언트가 신규 채팅방을 입력한 경우
		if self.room_num not in connectionStatus:
			connectionStatus[self.room_num] = {}
			connectionStatus[self.room_num][conn] = self.nickname
			conn.send('Y'.encode())
			print(f"[INFO] [room_num_{self.room_num}] {self.nickname}님 접속")
			for sock in connectionStatus[self.room_num]:
				if sock != conn: 
					sock.send(f"[INFO] {self.nickname}님 접속".encode())
		# 클라이언트가 기존 채팅방을 입력한 경우
		else:  															
			try:
				if self.nickname not in connectionStatus[self.room_num].values(): # 같은 채팅방 안에 중복 닉네임이 있는지 여부 판단 		
					connectionStatus[self.room_num][conn] = self.nickname
					conn.send('Y'.encode())	# 클라이언트에게 닉네임 등록 메시지 전달
					print(f"[INFO] [room_num_{self.room_num}] {self.nickname}님 접속")
					for sock in connectionStatus[self.room_num]:
						if sock != conn: 
							sock.send(f"[INFO] {self.nickname}님 접속".encode())
				else:
					raise OverlappedError # 중복닉네임 있으면 에러메시지 전달
			except OverlappedError as e:
				conn.send(f'{e}'.encode())

	def manage_message(self, data):
		global connectionStatus
		room_num = self.find_room_num(connectionStatus, conn)
		connection_dict = connectionStatus[room_num]

		if data.split(' ')[1] == '!whisper':
			sender_conn = conn
			receiver = data.split(' ')[2]
			if receiver in connection_dict.values():
				receiver_conn = self.find_conn(connection_dict, receiver)
				msg = data.split(' ')[3:]
				msg = ' '.join(msg)
				sender_nick = self.find_nick(connection_dict, sender_conn)  # conn으로 nick 찾기
				receiver_conn.send(f"(귓속말){sender_nick}{time_str}: {msg}".encode())
			else:
				receiver_conn.send(f"입력하신 닉네임은 존재하지 않습니다.".encode())

		elif data.split(' ')[1] == '!change_nick':
			changed_nick = data.split(' ')[2]
			original_conn = conn
			original_nick = self.find_nick(connection_dict, original_conn)  # conn으로 nick 찾기
			connection_dict[original_conn] = changed_nick  # conn의 value에 새로운 nick로 갱신
			msg = {'changed_nick': changed_nick}
			original_conn.send(json.dumps(msg).encode())
			for sock in connection_dict.keys():
				if sock != original_conn:   # 닉네임을 바꾼 클라이언트를 제외한 채팅방 멤버에게 메시지 전달
					sock.send(f"[INFO] {original_nick}님이 {changed_nick}로 닉네임 변경".encode())

		elif data.split(' ')[1] == '!member':
			member_list = list(connection_dict.values())
			conn.send(f'{member_list}'.encode())

		else: 
			msg = data
			for sock in connection_dict:
				sock.send(msg.encode())
				print(f'[MESSAGE] {data}')


HOST = '127.0.0.1'
PORT = 9111
ADDR = (HOST, PORT)

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # AF_INET = IPv4, SOCK_STREAM = TCP 통신
server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_sock.bind(ADDR)

server_sock.listen()

print("==============================================")
print(f"채팅 서버를 시작합니다. {PORT} 포트로 접속을 기다립니다.")
print("==============================================")

connectionStatus = {}  # 채팅방별 클라이언트 소켓, 닉네임 저장  ex) {1: {conn1: nick1, conn2: nick2, ...}, 2: {conn1: nick1, conn2:nick2, ...}, ...}

chat_room = ChatRoom()

connection_list = [server_sock]

while True:
	now = datetime.datetime.now()
	time_str = now.strftime('[%H:%M]')
	try:
		read_sockets, write_sockets, error_sockets = select(connection_list, [], [], 1)
		print("클라이언트 요청 대기...")
		for sock in read_sockets:
			if sock == server_sock:   # 새로운 클라이언트의 소켓이라면 connection_list에 추가
				newsock, addr = server_sock.accept()
				connection_list.append(newsock)
			else:    # 이미 접속한 클라이언트의 소켓이라면 클라이언트가 보낸 메시지 수신
				conn = sock
				data = conn.recv(1024).decode()

				if 'room_num' not in data:  # 이미 접속한 클라이언트의 메시지 수신
					try:
						chat_room.manage_message(data)  # 클라이언트의 메시지에 command가 있으면 해당 내용 수행, 없으면 메시지 자체를 broadcast
					except Exception as e:
						connection_list.remove(conn)

				else:  						# "최초" 접속한 클라이언트의 정보 수신
					login_info = json.loads(data)  # json 문자열인 data를 -> json.loads(data) -> 파이썬 객체(dict)
					try:
						chat_room.manage_client(conn, login_info)
					except Exception as e:
						print(e)

	except Exception as e:
		print(e)
		server_sock.close()
		sys.exit()
