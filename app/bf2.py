import socket

msg = bytes.fromhex('fefd00d8f30600ffffff01')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.settimeout(1)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# sock.bind(('192.168.56.1',0))

try:
    sock.sendto(msg, ('192.168.56.205', 29900))

    data, addr = sock.recvfrom(2000)

    data = data.replace(b'\x00', b' ').decode(errors='ignore')
    sock.close()

    servername = data.split('hostname')[-1].split('gamename', 1)[0].strip()
    maxpalyers = data.split('maxplayers')[-1].strip().split(' ', 1)[0]
    numplayers = data.split('numplayers')[-1].strip().split(' ', 1)[0]
    print(addr, servername, numplayers, maxpalyers)
except TimeoutError:
    print('pc_up{game=bf2} 0')
