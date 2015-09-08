#!/usr/bin/env python
# -*-*- encoding: utf-8 -*-*-
# Created: Tue, 01 Sep 2015 14:09:16 -0300

"""
Webserver
"""

import cgi


__authors__ = (
        'Christian Rollmann',
        'Isaac Mitsuaki Saito',
        'Julio Batista Silva',
        'Marcelo Fernandes Tedeschi',)
__license__ = "GPL"
__version__ = "1.0"


# CGI header
print "Content-type: text/html\n\n"


# Imprime a versão do python, as variáveis de ambiente e as mensagens do cgitb
DEBUG = True
DEBUG_PRINT = False
if DEBUG:
    import sys
    import os
    import cgitb
    cgitb.enable()


form = cgi.FieldStorage()
m1 = form.getlist("m1")  # Lista da máquina 1
m2 = form.getlist("m2")  # Lista da máquina 2


print """
<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="utf-8">
    <title>Redes - Projeto 1</title>
  </head>
  <body>
    <header>
      <h1>Projeto 1</h1>
    </header>
<form name="comandos" method="post" action="webserver.py">
  <label>Máquina 1: </label>
  <label><input type="checkbox" name="m1" value="ps">ps</label>
  <label><input type="checkbox" name="m1" value="df">df</label>
  <label><input type="checkbox" name="m1" value="finger">finger</label>
  <label><input type="checkbox" name="m1" value="uptime">uptime</label>
  <label><input type="checkbox" name="m1" value="rm" disabled>rm -rf /</label>
  <br>
  <label>Máquina 2: </label>
  <label><input type="checkbox" name="m2" value="ps">ps</label>
  <label><input type="checkbox" name="m2" value="df">df</label>
  <label><input type="checkbox" name="m2" value="finger">finger</label>
  <label><input type="checkbox" name="m2" value="uptime">uptime</label>
  <br>
  <button type="submit" name="Enviar">Enviar</button>
</form>
<h3>Comandos Enviados:</h3>
"""


print "<p>Máquina 1: {}</p>".format(", ".join(m1))
print "<p>Máquina 2: {}</p>".format(", ".join(m2))


if DEBUG:
    print '<div id="debug" style="display: {};">'.format("block" if DEBUG_PRINT else "none")
    print "<hr><h3>Debug</h3><pre>"
    print "Versão do Python: {}<br>".format(sys.version)
    for param in os.environ.keys():
        print "{:<30} = {}".format(param, os.environ[param])
    print "</pre><hr></div>"


print "</body></html>"
