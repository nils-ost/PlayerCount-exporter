import socket


def bf2(ip, port):
    iname, numplayers, maxplayers, up = ('', 0, 0, 0)

    msg = bytes.fromhex('fefd00d8f30600ffffff01')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.settimeout(0.5)
    try:
        sock.sendto(msg, (ip, port))
        data, addr = sock.recvfrom(2000)
        sock.close()
        data = data.replace(b'\x00', b' ').decode(errors='ignore')

        iname = data.split('hostname')[-1].split('gamename', 1)[0].strip()
        maxplayers = data.split('maxplayers')[-1].strip().split(' ', 1)[0]
        numplayers = data.split('numplayers')[-1].strip().split(' ', 1)[0]
        up = 1
    except TimeoutError:
        pass

    return (iname, up, numplayers, maxplayers)


def ut2k4(ip, port):
    iname, numplayers, maxplayers, up = ('', 0, 0, 0)

    msg = bytes.fromhex('8000000000')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.settimeout(0.5)
    try:
        sock.sendto(msg, (ip, port))
        data, addr = sock.recvfrom(200)
        sock.close()

        iname = data[19:18 + data[18]].decode(errors='ignore')
        maxplayers = data[-17]
        numplayers = data[-21]
        up = 1
    except TimeoutError:
        pass

    return (iname, up, numplayers, maxplayers)
