import socket
import psycopg2

CHECK_ACTIVE = """SELECT * FROM subscribers where is_subscribed ='True';"""
CHECK_FALSE = """SELECT * FROM subscribers where is_subscribed ='False';"""

class Client:
    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout

    def _send(self, message):
        with socket.create_connection((self.host, self.port), self.timeout) as sock:
            try:
                sock.sendall(message.encode("utf8"))
                data = sock.recv(1024)
                print(data.decode())
            except socket.timeout:
                print("send data timeout")
            except socket.error as ex:
                print("send data error:", ex)

    def __call__(self, message):
        self._send(message)
        print("Отправка метрики в БД. Событие: использован метод _send.")



conn = psycopg2.connect(
            host='127.0.0.1',
            user='postgres',
            password='123',
            database='data'
        )



client = Client("127.0.0.1", 5000, timeout=15)
while True:
    user_answer = input("Нажмите 1 для активации всех подписок \nНажмите 2 для деактивации всех подписок \n")
    if user_answer == '1':
        with conn.cursor() as cursor:
            cursor.execute(CHECK_ACTIVE)
            row = cursor.fetchall()
            conn.commit()
        client(str(row))
    if user_answer == '2':
        with conn.cursor() as cursor:
            cursor.execute(CHECK_FALSE)
            row = cursor.fetchall()
            conn.commit()
        client(str(row))
    else:
        break