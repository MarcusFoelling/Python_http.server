# Python_http.server
Opens a listener (web server) on given TCP port, useful for firewall testing

Usage:

[sudo] python3 ./server.py [port]


for a list of ports specified in portlist.txt

for port in $(cat portlist.txt); do sudo python3 ./server.py $port & done
