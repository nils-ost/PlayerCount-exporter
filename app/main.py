import cherrypy


class PlayerCountExporter():
    def __init__(self):
        self.bf2 = bf2()


@cherrypy.popargs('node', 'port')
class bf2():
    @cherrypy.expose()
    def index(self, node='127.0.0.1', port=29900):
        cherrypy.response.headers['Cache-Control'] = 'no-cache'
        cherrypy.response.headers['Content-Type'] = 'text/plain; version=0.0.4'
        return ''


if __name__ == '__main__':
    conf = {}
    cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': 8080})
    cherrypy.quickstart(PlayerCountExporter(), '/', conf)