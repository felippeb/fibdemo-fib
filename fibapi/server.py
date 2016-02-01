from gevent.wsgi import WSGIServer
from fibapi import fibapi

http_server = WSGIServer(('', 5000), fibapi.app)
http_server.serve_forever()
