import time
import socket

from cloudify.state import ctx_parameters as inputs

def wait_for_http(server_ip):
    s = socket.socket()
    address = server_ip
    port = 80
    while True:
        time.sleep(5)
        try:
            s.connect((address, port))
            return
        except Exception as e:
            pass

wait_for_http(inputs['host'])
