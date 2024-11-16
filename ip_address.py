import socket

def get_ip(url):
    return socket.gethostbyname(url)


