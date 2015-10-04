#!/usr/bin/env python2
# -*-*- encoding: utf-8 -*-*-
# Created: Thu, 24 Sep 2015 14:28:56 -0300

"""
Daemon
"""

from __future__ import division
from __future__ import print_function

import sys
import socket
import threading
import argparse
from subprocess import check_output, STDOUT
from unidecode import unidecode

from util import get_host_ip, cmd_name


__authors__ = (
    'Christian Rollmann',
    'Isaac Mitsuaki Saito',
    'Julio Batista Silva',
    'Marcelo Fernandes Tedeschi',)
__license__ = "GPL v3"
__version__ = "1.0"


class ClientHandler(threading.Thread):

    def __init__(self, (socket, address)):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address

    # Clean arguments to make the command safe
    def clean_arg(self, message):
        try:
            from shlex import quote as cmd_quote # Python 3.3
        except ImportError:
            from pipes import quote as cmd_quote

        malicious = set('^|;<>&')
        if any((c in malicious) for c in message):
            return ''
        else:
            return cmd_quote(message)


    def run(self):
        while True:
            message = self.socket.recv(2**16)

            if not message:
                print("Empty message. Fechando o socket")
                self.socket.close()
                break

            print("Recebi de '{}': '{}'".format(self.address[0], message))
            tipo, cmd, arg = message.split(' ', 2)
            print("Tipo: '{}', cmd: '{}', arg: '{}'".format(tipo, cmd, arg))

            if tipo == 'REQUEST':
                full_cmd = cmd_name(cmd)

                if arg:
                    full_cmd += " " + self.clean_arg(arg)

                print("Rodando: `{}`".format(full_cmd))
                saida = check_output(full_cmd, stderr=STDOUT, shell=True)
                header = unidecode("RESPONSE " + cmd + " " + saida)
                print("Enviando `{}` para {}".format(header, self.address[0]))
                self.socket.sendall(header)


class Server:
    def __init__(self, address):
        self.host = address[0]
        self.port = address[1]
        self.server = None

    def open_socket(self):
        try:
            print("Opening '{}':'{}'".format(self.host, self.port))
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            clientHandler = ClientHandler(self.server.accept())
            clientHandler.start()
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
