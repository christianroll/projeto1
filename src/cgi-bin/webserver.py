#!/usr/bin/env python
# -*-*- encoding: utf-8 -*-*-
# Created: Tue, 01 Sep 2015 14:09:16 -0300

"""
Webserver and Backend
"""

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import cgi
import cgitb
import struct

import os
import socket

from view import serve_template
from settings import maquinas

__authors__ = (
    'Christian Rollmann',
    'Isaac Mitsuaki Saito',
    'Julio Batista Silva',
    'Marcelo Fernandes Tedeschi',)
__license__ = "GPL"
__version__ = "1.0"

def send_one_message(sock, data):
    length = len(data)
    sock.sendall(struct.pack('<H', length))
    sock.sendall(data)

def recv_one_message(sock):
    lengthbuf = recvall(sock, 4)
    length, = struct.unpack('<H', lengthbuf)
    return recvall(sock, length)


def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf




cgitb.enable()


# CGI header
print("Content-type: text/html\n\n")

respostas = True if os.environ['REQUEST_METHOD'] == 'POST' else False


# "Backend". Executado após form ser submetido.
if respostas:
    form = cgi.FieldStorage()
    # Envia os comandos para cada uma das máquinas e espera resposta
    print("<pre>")
    for m in maquinas:
        m['cmds'] = form.getlist(m['ip'])

        # Cria um socket TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Conecta o socket à porta que a máquina está escutando
        print("Conectando-me a {} na porta {}".format(m['ip'], m['porta']))
        server_address = (m['ip'], m['porta'])
        sock.connect(server_address)

        m['respostas'] = []
        for cmd in m['cmds']:
            try:
                # Envia
                print("Enviando `{}` para {}".format(cmd, m['ip']))
                send_one_message(sock, cmd)
                # Recebe
                resposta = recv_one_message(sock)
                m['respostas'].append(resposta)
                print('Recebi: {}'.format(resposta))
            finally:
                print('Fechando socket')
                sock.close()
    print("</pre>")

serve_template('index.mako',
               autores=", ".join(__authors__),
               maquinas=maquinas,
               respostas=respostas)
