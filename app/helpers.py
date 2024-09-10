

def generate_output(game, ingamename, up, numplayers, maxplayers):
    lines = list()
    lines.append('# HELP playercount_up if the game-server responded to the request of collecting data')
    lines.append('# TYPE playercount_up gauge')
    lines.append(f'playercount_up{{game="{game}",iname="{ingamename}"}} {up}')
    lines.append('# HELP playercount_num number of players currently on server')
    lines.append('# TYPE playercount_num gauge')
    lines.append(f'playercount_num{{game="{game}",iname="{ingamename}"}} {numplayers}')
    lines.append('# HELP playercount_max maximum allowed players on server')
    lines.append('# TYPE playercount_max gauge')
    lines.append(f'playercount_max{{game="{game}",iname="{ingamename}"}} {maxplayers}')
    return '\n'.join(lines)
