import socket
from const import HOST_PORT_PAIR
import json

sock = socket.create_connection(HOST_PORT_PAIR)

m = {'number': 1, 'second_number': 2}
data = json.dumps(m)

with sock:
    while True:
        text = input('CLIENT 1 ---- Enter data or js for json file or q for exit: ')
        if text.lower() == 'q':
            break
        elif text.lower() == 'js':
            sock.send(data.encode())
        else:
            sock.send(text.encode())
