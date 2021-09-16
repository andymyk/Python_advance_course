import socket
from const import HOST_PORT_PAIR
import json

sock = socket.create_connection(HOST_PORT_PAIR)

m = {'number': 1, 'second_number': 2}
data = json.dumps(m)

with sock:
    sock.sendall(data.encode())
