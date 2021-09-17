import asyncio
import psycopg2


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    async def handle_echo(self, reader, writer):
        data = await reader.read(1024)
        message = data.decode()
        message = eval(message)
        Server.database(self,message)
        print('Connect to DB')
        addr = writer.get_extra_info('peername')
        print(addr)
        print('received %r from %r' % (message, addr))
        writer.write(f"echo server - {message}".encode())

        writer.close()

    def run_server(self):
        """Запускает сервер в вечном цикле"""
        loop = asyncio.get_event_loop()
        coro = asyncio.start_server(client_connected_cb=self.handle_echo, host=self.host, port=self.port,
                                    loop=loop)  # передали параметры
        loop.run_until_complete(coro)

        try:
            loop.run_forever()
        except KeyboardInterrupt:
            print("Server stopped by keyboard")
            loop.close()

    def database(self,message):
        conn = psycopg2.connect(
            host='127.0.0.1',
            user='postgres',
            password='123',
            database='data'
        )
        with conn.cursor() as cursor:
            for i in message:
                if i[1] == 'False':
                    cursor.execute(f"""UPDATE subscribers SET is_subscribed = 'True' where username = '{i[0]}';""")
                    conn.commit()

serv = Server(host='127.0.0.1', port=5000)
serv.run_server()