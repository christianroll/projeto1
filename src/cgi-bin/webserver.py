#!/usr/bin/env python
# -*-*- encoding: utf-8 -*-*-
# Created: Tue, 01 Sep 2015 14:09:16 -0300

"""
Webserver
"""

# from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import cgi
import cgitb

from view import serve_template
from settings import maquinas


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

form = cgi.FieldStorage()

# Envia os comandos para cada uma das máquinas e espera resposta
respostas = []
print("<pre>")
for m in maquinas:
    m['cmds'] = form.getlist(m['ip'])
    for cmd in m['cmds']:
        print('Enviando `{}` para "{}"'.format(cmd, m['ip']))
        resposta = "TODO"
        respostas.append(resposta)
print("</pre>")


serve_template('index.mako',
               autores=", ".join(__authors__),
               maquinas=maquinas,
               respostas=respostas)
