# -*- coding: utf-8 -*-
#!/usr/bin/env python3
port=8100
from http.server import HTTPServer, CGIHTTPRequestHandler
server_address = ("", port)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
print("server strated ", port)
httpd.serve_forever()
