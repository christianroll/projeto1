#!/usr/bin/env python2
# -*-*- encoding: utf-8 -*-*-
# Created: Thu, 24 Sep 2015 14:28:56 -0300

"""
Daemon
"""

from __future__ import division
from __future__ import print_function

import socket
import struct
import sys
from thread import *
from subprocess import check_output
from subprocess import STDOUT

__authors__ = (
    'Christian Rollmann',
    'Isaac Mitsuaki Saito',
    'Julio Batista Silva',
    'Marcelo Fernandes Tedeschi',)
__license__ = "GPL v3"
__version__ = "1.0"


def send_one_message(sock, data):
    length = len(data)
    sock.sendall(struct.pack('<H', length))
    sock.sendall(data)

def recv_one_message(sock):
    lengthbuf = recvall(sock, 4)
    length, = struct.unpack('<H',lengthbuf)
    return recvall(sock, length)


def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def clientthread(connection,client_address):
    #infinite loop so that function do not terminate and thread do not end.
    while True:
        #Receiving from client
        cmd=recv_one_message(connection)
	#if not buf:
        #     break
        print("Recebi: {} de {}".format(cmd, client_address))
        allowed_cmds = ['df', 'finger', 'ps', 'uptime']
        if cmd in allowed_cmds:
              saida = check_output(cmd, stderr=STDOUT, shell=True)
        else:
              saida = "Comando invalido!"
        send_one_message(connection, saida)
    connection.close()


# IP e porta da máquina local
ip = '10.37.129.3'
porta = 10000


# Cria o socket TCP/IP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind
server_address = (ip, porta)
try:
    sock.bind(server_address)
except socket.error , msg:
    print ("Bind failed. Error Code : {} Message: {}".format(str(msg[0]), msg[1]))
    sys.exit()


# Fica na escuta aguardando conexões
sock.listen(10)


#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    connection, client_address = sock.accept()
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(connection,client_address))



