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

DEBUG = ''

respostas = True if os.environ['REQUEST_METHOD'] == 'POST' else False

class ConnectionThread(threading.Thread):
    def __init__(self, m, index, queue):
        #print("Nova Thread")
        threading.Thread.__init__(self)
        self.m = m
        self.q = queue
        self.index = index


        
    def run(self):

        d = {}
        d['ip'] = self.m['ip']
        d['index'] = self.index
        d['respostas'] = []


        # Envia os comandos para cada uma das máquinas e espera resposta
        for cmd in self.m['cmds']:
            arg = form.getfirst(self.m['ip'] + "_arg" + str(cmd))
            
            #print(self.m['ip'])
            #print(self.m['porta'])


            try:
                # Cria um socket TCP/IP
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # Conecta o socket à porta que a máquina está escutando
                # DEBUG += "Conectando-me a {} na porta {}\n".format(m['ip'], m['porta'])
                server_address = (self.m['ip'], self.m['porta'])

                sock.connect(server_address)
                # DEBUG += "Conectou a {} na porta {}\n".format(m['ip'], m['porta'])    
                if arg is None:
                    arg = ''
                header = "REQUEST " + cmd + " " + arg

                sock.sendall(unidecode(header.decode()))
                # Recebe
                resposta = sock.recv(65536)

                try:
                    cmd, saida = resposta.split(None, 2)[1:]

                except:
                    # TODO: FIXME
                    #cmd = resposta.split(None, 2)[1]
                    cmd = ''
                    saida = ''

                d['respostas'].append(["Maquina: "+self.m['ip']+", Comando: " + cmd_name(cmd), saida])

            finally:
                # DEBUG += 'Fechando socket\n'
                sock.close()
        self.q.put(d)


# "Backend". Executado após form ser submetido.

if respostas:

    queue = Queue.Queue()

    form = cgi.FieldStorage()

    threads = []
    for (index, m) in enumerate(maquinas):
        m['cmds'] = form.getlist(m['ip'])
        thread = ConnectionThread(m, index, queue)
        thread.start()
        threads.append(thread)

    for t in threads:
        t.join()

    while not queue.empty():
        rsp = queue.get()
        maquinas[rsp['index']]['respostas'] = rsp['respostas']
        





    





            

serve_template('index.mako',
               autores=", ".join(__authors__),
               maquinas=maquinas,
               comandos=comandos,
               respostas=respostas,
               DEBUG=DEBUG)
