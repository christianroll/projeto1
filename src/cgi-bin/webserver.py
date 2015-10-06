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
import threading
import os
import socket
import Queue

from unidecode import unidecode

from view import serve_template
from settings import maquinas
from util import cmd_name, comandos

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


class ConnectionThread(threading.Thread):
    def __init__(self, m, index, queue):

        threading.Thread.__init__(self)
        self.m = m
        self.q = queue
        self.index = index

    def run(self):
        # Dictionary to deal with queue for multiples threads
        d = {}
        d['ip'] = self.m['ip']
        d['index'] = self.index
        d['respostas'] = []

        # For each command from each machine, create a socket connection
        for cmd in self.m['cmds']:
            arg = form.getfirst(self.m['ip'] + "_arg" + str(cmd))

            try:
                # Creates a TCP/IP socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # Connects the socket to the machine listening door
                server_address = (self.m['ip'], self.m['porta'])
                sock.connect(server_address)
                # Check is there is any arg to be sent
                if arg is None:
                    arg = ''
                header = "REQUEST " + cmd + " " + arg
                sock.sendall(unidecode(header.decode()))
                # Wait for answer from daemon
                resposta = sock.recv(65536)
                # Eg.: Response 1 "answer"
                try:
                    # Eg.: cmd = 1 saida ="answer"
                    cmd, saida = resposta.split(None, 2)[1:]

                except:
                    # TODO: FIXME
                    # cmd = resposta.split(None, 2)[1]
                    cmd = ''
                    saida = ''
                # Put answer from server in dicionary 
                d['respostas'].append(["Maquina: " + self.m['ip'] +
                                       ", Comando: " + cmd_name(cmd), saida])

            finally:
                sock.close()
        # Put dictionary in queue       
        self.q.put(d)


# "Backend". Runs after form submission.
if respostas:
    # Create queue for deal with data inside threads and return it in main()
    queue = Queue.Queue()
    # Create instance of FieldStorage
    form = cgi.FieldStorage()

    threads = []
    # Inicialize thread for each machine
    for (index, m) in enumerate(maquinas):
        m['cmds'] = form.getlist(m['ip'])
        thread = ConnectionThread(m, index, queue)
        thread.start()
        threads.append(thread)

    # Wait each thread finish
    for t in threads:
        t.join()

    # Get queue values witch client answers
    while not queue.empty():
        rsp = queue.get()
        # Pass queue answers to form list to be displayed in web
        maquinas[rsp['index']]['respostas'] = rsp['respostas']


serve_template('index.mako',
               autores=", ".join(__authors__),
               maquinas=maquinas,
               comandos=comandos,
               respostas=respostas,
               )
