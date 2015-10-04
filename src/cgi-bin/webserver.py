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

import os
import socket

from unidecode import unidecode

from view import serve_template
from settings import maquinas
from util import cmd_name

__authors__ = (
    'Christian Rollmann',
    'Isaac Mitsuaki Saito',
    'Julio Batista Silva',
    'Marcelo Fernandes Tedeschi',)
__license__ = "GPL"
__version__ = "1.0"


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
        print("Conectou a {} na porta {}".format(m['ip'], m['porta']))

        m['respostas'] = []
        for cmd in m['cmds']:
            arg = form.getfirst(m['ip'] + "_arg" + str(cmd))
            print("cmd = '{}'; arg: '{}'".format(cmd, arg))

            try:
                # Envia
                header = unidecode("REQUEST " + cmd + " " + arg)
                print("Enviando `{}` para {}:{}".format(header, m['ip'], m['porta']))
                sock.sendall(header)
                # Recebe
                resposta = sock.recv(65536)
                print('Recebi: {}'.format(resposta))
                cmd, saida = resposta.split(None, 2)[1:]
                m['respostas'].append((cmd_name(cmd), saida))
            finally:
                print('Fechando socket')
                sock.close()
    print("</pre>")

serve_template('index.mako',
               autores=", ".join(__authors__),
               maquinas=maquinas,
               respostas=respostas)
