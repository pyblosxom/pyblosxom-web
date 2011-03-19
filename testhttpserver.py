#!/usr/bin/python

import SimpleHTTPServer
import BaseHTTPServer
import os
import os.path

def run(address="localhost", port=8000, dir="."):
    os.chdir(os.path.join(os.getcwd(), dir))
    server_class = BaseHTTPServer.HTTPServer
    handler_class = SimpleHTTPServer.SimpleHTTPRequestHandler
    server_address = (address, port)
    print "Serving files under %s" % os.getcwd()
    print "URL: http://%s:%d/" % (address, port)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    try:
        run("localhost", 8000, "./compiled_site/")
    except KeyboardInterrupt, ki:
        print "Shutting down...."
