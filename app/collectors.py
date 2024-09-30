import socket
import json


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


def ut3(ip, port):
    iname, numplayers, maxplayers, up = ('', 0, 0, 0)
    ip = '255.255.255.255'  # Needs to be broadcast in this case
    msg = bytes.fromhex('05014d5707db53514e694a4f73504345')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(1)
    try:
        sock.sendto(msg, (ip, port))
        data, addr = sock.recvfrom(2000)
        sock.close()
        print(data)

        iname = data[61:61 + data[60]].decode(errors='ignore')
        maxplayers = data[35]
        numplayers = maxplayers - data[27]
        up = 1
    except TimeoutError:
        pass

    return (iname, up, numplayers, maxplayers)


def mc(ip, port):
    iname, numplayers, maxplayers, up = ('', 0, 0, 0)
    data = None

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.settimeout(0.5)
            sock.connect((ip, port))
            msg_len = hex(len(sock.getpeername()[0]) + 7).replace('0x', '')
            msg_len = bytes.fromhex(msg_len if len(msg_len) == 2 else '0' + msg_len)
            ip_len = hex(len(sock.getpeername()[0])).replace('0x', '')
            ip_len = bytes.fromhex(ip_len if len(ip_len) == 2 else '0' + ip_len)
            msg = msg_len + bytes.fromhex('00ff05') + ip_len + sock.getpeername()[0].encode() + bytes.fromhex('63dd01')
            sock.sendall(msg)
            msg = bytes.fromhex('0100')
            sock.sendall(msg)
            data = sock.recv(2000)

            data = json.loads('{' + data.replace(b'\x00', b' ').decode(errors='ignore').split('{', 1)[-1].rsplit('}', 1)[0] + '}')
            iname = data.get('description', '')
            if isinstance(iname, dict) and 'text' in iname:
                iname = iname['text']
            maxplayers = data.get('players', dict()).get('max', 0)
            numplayers = data.get('players', dict()).get('online', 0)
            up = 1
        except TimeoutError:
            pass

    return (iname, up, numplayers, maxplayers)


def cod2(ip, port):
    iname, numplayers, maxplayers, up = ('', 0, 0, 0)

    msg = bytes.fromhex('ffffffff676574696e666f20787878')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.settimeout(0.5)
    try:
        sock.sendto(msg, (ip, port))
        data, addr = sock.recvfrom(2000)
        sock.close()
        data = data.replace(b'\x00', b' ').decode(errors='ignore').replace('\n', '').split('\\')

        for i in range(len(data)):
            if data[i] == 'hostname':
                iname = data[i + 1]
            if data[i] == 'clients':
                numplayers = data[i + 1]
            if data[i] == 'sv_maxclients':
                maxplayers = data[i + 1]
        up = 1
    except TimeoutError:
        pass

    return (iname, up, numplayers, maxplayers)


def cod4(ip, port):
    iname, numplayers, maxplayers, up = ('', 0, 0, 0)

    msg = bytes.fromhex('ffffffff676574696e666f20787878')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.settimeout(0.5)
    try:
        sock.sendto(msg, (ip, port))
        data, addr = sock.recvfrom(2000)
        sock.close()
        data = data.replace(b'\x00', b' ').decode(errors='ignore').replace('\n', '').split('\\')

        for i in range(len(data)):
            if data[i] == 'hostname':
                iname = data[i + 1]
            if data[i] == 'g_humanplayers':
                numplayers = data[i + 1]
            if data[i] == 'sv_maxclients':
                maxplayers = data[i + 1]
        up = 1
    except TimeoutError:
        pass

    return (iname, up, numplayers, maxplayers)
