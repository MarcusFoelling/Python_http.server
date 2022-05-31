#!/usr/bin/python
'''
    Opens a listener (web server) on given TCP port, useful for firewall testing
    Marcus Andreas Fölling - 31.05.2022
    v0.01
'''

# Imports
import sys
import http.server
import socketserver

# Main
def main():
    if len(sys.argv) > 1:
        Port = int(sys.argv[1])
    else:
        Port = 80

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(('', Port), Handler) as httpd:
        print("listening on port: %s, you may kill me with CTRL+C" % Port)
        httpd.serve_forever()

if __name__ == '__main__': 
    main()