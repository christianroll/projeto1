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
from subprocess import check_output
from subprocess import STDOUT

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

    def cmd_name(self, cmd):
        return{
           '1': 'ps',
           '2': 'df',
           '3': 'finger',
           '4': 'uptime'
        }.get(cmd, '')  # TODO:raise exception if invalid cmd

    # TODO: Clean arguments to make the command safe
    def clean_arg(self, message):
        malicious = set('^|;<>&')
        if any((c in malicious) for c in message):
            return ''
        else:
            return message

    def run(self):
        while True:
            message = self.socket.recv(2**16)

            if not message:
                self.server.close()
                print("Empty message. Fechando o socket")
                break

            print("Recebi de '{}': '{}'".format(self.address[0], message))
            tipo, cmd, arg = message.split(' ', 2)
            print("Tipo: '{}', cmd: '{}', arg: '{}'".format(tipo, cmd, arg))

            if tipo == 'REQUEST':
                full_cmd = self.cmd_name(cmd)

                if arg:
                    full_cmd += " " + self.clean_arg(arg)

                saida = check_output(full_cmd, stderr=STDOUT, shell=True)
                header = "RESPONSE " + cmd + " " + saida
                print("Enviando `{}` para {}:{}".format(header, self.address[0], self.address[1]))
                self.socket.sendall(header)


class SimpleServer:
    def __init__(self, address):
        self.host = address[0]
        self.port = address[1]
        self.server = None

    def open_socket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind((self.host, self.port))
            self.server.listen(5)
        except socket.error, (value, message):
            if self.server:
                self.server.close()
            print("Socket could not be opened: {}".format(message))
            sys.exit(1)

    def startListen(self):
        self.open_socket()
        while True:
            clientHandler = ClientHandler(self.server.accept())
            clientHandler.start()


address = ('10.0.0.6', 10000)

# Inicio do Script
SimpleServer(address).startListen()
