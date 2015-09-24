#!/usr/bin/env python2
# -*-*- encoding: utf-8 -*-*-
# Created: Thu, 24 Sep 2015 14:28:56 -0300

"""
Daemon
"""


from __future__ import division
from __future__ import print_function

import socket
from subprocess import check_output
from subprocess import STDOUT


__authors__ = (
        'Christian Rollmann',
        'Isaac Mitsuaki Saito',
        'Julio Batista Silva',
        'Marcelo Fernandes Tedeschi',)
__license__ = "GPL v3"
__version__ = "1.0"


# IP e porta da máquina local
ip = '10.0.0.3'
porta = 10000


# Cria o socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind
server_address = (ip, porta)
sock.bind(server_address)


# Fica na escuta aguardando conexões
sock.listen(1)


while True:
    connection, client_address = sock.accept()
    try:
        while True:
            cmd = connection.recv(4096)
            print("Recebi: {} de {}".format(cmd, client_address))
            allowed_cmds = ['df', 'finger', 'ps', 'uptime']
            if cmd in allowed_cmds:
                saida = check_output(cmd, stderr=STDOUT, shell=True)
            else:
                saida = "Comando invalido!"
            connection.sendall(saida)
    finally:
        connection.close()
