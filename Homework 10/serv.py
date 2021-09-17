import socket
from const import HOST_PORT_PAIR
from logging import getLogger
from datetime import datetime
import json

logger = getLogger(__name__)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(HOST_PORT_PAIR)
sock.listen(socket.SOMAXCONN)
conn, addr = sock.accept()

with conn, sock:
    while True:
        received_data = conn.recv(1024)
        received_data = received_data.decode('utf-8')
        logger.error(f"{datetime.now()}, {received_data}")
        with open('received_data.json', 'w') as f:
            json.dump(received_data, f)
