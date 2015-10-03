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
    saida = ''

    def set_cmd(cmd):
        return{
           '1': 'ps', 
           '2': 'ds', 
           '3': 'finger', 
           '4': 'uptime'
        }.get(cmd,0) #TODO:raise exception if invalid cmd
		
    #separa string recebida para analisar cada comando    
    def separa_string(message):
        separa=message.split(' ')
        if separa[0]=='REQUEST':
            cmd=set_cmd(separa[1]) + " " #+ parametro

    def __init__(self, socket, address):
        threading.Thread.__init__(self)
        self.socket = socket
        self.address = address

    def run(self):
        message = self.socket.recv(4096)
        while True:
    	    print("Recebi do cliente:{} -: {}".format(self.address[0], message))
            separa_string(message)
    	    saida = check_output(cmd, stderr=STDOUT, shell=True)
    	    resp = self.socket.send(saida)
        self.socket.close()
 

class SimpleServer:
    def __init__(self, portNumber):
        self.portNumber = portNumber

    def startListen(self):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind( ('10.37.129.3', self.portNumber) )
        serverSocket.listen(5)
        
        while True:
            clientSocket, address = serverSocket.accept()
            clientHandler = ClientHandler(clientSocket, address)
            clientHandler.start()

porta = 10000

#Inicio do Script
SimpleServer(porta).startListen()



