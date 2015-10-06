#!/usr/bin/env python2
# -*-*- encoding: utf-8 -*-*-
# Created: Thu, 24 Sep 2015 14:28:56 -0300

"""
Daemon
"""

from __future__ import division
from __future__ import print_function

import re
import sys
import socket
import threading
import argparse
from subprocess import check_output, STDOUT, CalledProcessError
from unidecode import unidecode

from util import get_host_ip, cmd_name

__authors__ = (
    'Christian Rollmann',
    'Isaac Mitsuaki Saito',
    'Julio Batista Silva',
    'Marcelo Fernandes Tedeschi',)
__license__ = "GPL v3"
__version__ = "1.0"


# Class that deal with client requests
class ClientHandler(threading.Thread):
    def __init__(self, (socket, address)):
        print("Nova Thread")
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address
        self.socket.settimeout(60)

    # Clean arguments to make the command safe
    def clean_arg(self, message):
        whitelist = '[^\w .,\-\=]+'
        return re.sub(whitelist, '', message)

    def run(self):
        try:
            while True:
                message = self.socket.recv(2 ** 16).decode()
                message = re.sub(r"\r\n", "", message)

                if not message:
                    print("Empty message. Fechando o socket")
                    self.socket.close()
                    break

                print("Recebi de '{}': '{}'".format(self.address[0], message))

                # Eg.: message = "REQUEST 1 -j"
                try:
                    tipo, cmd, arg = message.split(' ', 2)

                # Eg.: message = "REQUEST 1"
                except:
                    try:
                        tipo, cmd = message.split(' ')
                        arg = ''

                    # Eg.: message = "REQUEST"
                    except:
                        header = "HTTP/1.1 400 Bad Request\r\n" \
                                 "Connection: close\r\n\r\n"
                        print("Enviando `{}` para {}".format(header, self.address[0]))
                        self.socket.sendall(unidecode(header.decode()))
                        print("Fechando o socket")
                        self.socket.close()
                        break

                print("Tipo: '{}', cmd: '{}', arg: '{}'".format(tipo, cmd, arg))

                # Only request method allowed
                if tipo == 'REQUEST':
                    full_cmd = cmd_name(cmd)
                    # Verify if there is any argument
                    if arg:
                        full_cmd += " " + self.clean_arg(arg)
                    print("Rodando: `{}`".format(full_cmd))
                    try:
                        saida = check_output(full_cmd, stderr=STDOUT, shell=True)
                    except CalledProcessError, e:
                        saida = e.output
                    header = "RESPONSE " + cmd + " " + saida
                    print("Enviando `{}` para {}".format(header, self.address[0]))
                    self.socket.sendall(unidecode(header.decode()))

                # Returns 405 if receive a GET, POST, HEAD, PUT, OPTIONS, etc
                # Could also be 501 Method Not Implemented
                else:
                    header = "HTTP/1.1 405 Method Not Allowed\r\n" \
                             "Allow: REQUEST\r\n" \
                             "Connection: close\r\n\r\n"
                    print("Enviando `{}` para {}".format(header, self.address[0]))
                    self.socket.sendall(unidecode(header.decode()))
                    print("Fechando o socket")
                    self.socket.close()
                    break

        except Exception, e:
            print("Error: '{}'".format(e))
            print("Fechando o socket")
            self.socket.close()


# Class that prepare socket for listening
class Server:
    def __init__(self, address):
        self.host = address[0]
        self.port = address[1]
        self.server = None

    def open_socket(self):
        try:
            print("Opening '{}':'{}'".format(self.host, self.port))
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.server.bind((self.host, self.port))
            self.server.listen(5)
        except socket.error, (value, message):
            if self.server:
                self.server.close()
            print("Socket could not be opened: {}".format(message))
            sys.exit(1)

    def start_listen(self):
        self.open_socket()
        while True:
            # Call a thread for each client connection
            ClientHandler(self.server.accept()).start()
        # Never gets here!
        print("Turning off server?")
        self.server.close()


def main(args):
    address = (args.host, args.port)
    Server(address).start_listen()
    return 0


if __name__ == "__main__":
    host = get_host_ip()[-1]
    parser = argparse.ArgumentParser(description='Daemon.')
    parser.add_argument('--host', default=host, help='Daemon IP address')
    parser.add_argument('-p', '--port', type=int, default=9001, help='Port')
    args = parser.parse_args()

    sys.exit(main(args))
