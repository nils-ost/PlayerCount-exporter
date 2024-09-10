import socket

msg = bytes.fromhex('8000000000')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.settimeout(1)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# sock.bind(('192.168.56.1',0))

try:
    sock.sendto(msg, ('192.168.56.220', 10777))

    data, addr = sock.recvfrom(200)
    sock.close()

    servername = data[19:18 + data[18]].decode(errors='ignore')
    maxpalyers = data[-17]
    numplayers = data[-21]
    print(addr, servername, numplayers, maxpalyers)
except TimeoutError:
    print('timeout')
