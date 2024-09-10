import cherrypy
from helpers import generate_output


class PlayerCountExporter():
    def __init__(self):
        self.bf2 = bf2()
        self.ut2k4 = ut2k4()


@cherrypy.popargs('ip', 'port')
class bf2():
    @cherrypy.expose()
    def index(self, ip='127.0.0.1', port=29900):
        from collectors import bf2
        cherrypy.response.headers['Cache-Control'] = 'no-cache'
        cherrypy.response.headers['Content-Type'] = 'text/plain; version=0.0.4'
        iname, up, numplayers, maxplayers = bf2(ip, port)
        return generate_output('bf2', iname, up, numplayers, maxplayers)


@cherrypy.popargs('ip', 'port')
class ut2k4():
    @cherrypy.expose()
    def index(self, ip='127.0.0.1', port=29900):
        from collectors import ut2k4
        cherrypy.response.headers['Cache-Control'] = 'no-cache'
        cherrypy.response.headers['Content-Type'] = 'text/plain; version=0.0.4'
        iname, up, numplayers, maxplayers = ut2k4(ip, port)
        return generate_output('ut2k4', iname, up, numplayers, maxplayers)


if __name__ == '__main__':
    conf = {}
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})
    cherrypy.quickstart(PlayerCountExporter(), '/', conf)
