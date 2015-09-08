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
m1 = form.getlist("m1")  # Lista da máquina 1
m2 = ["maquina1", "maquina2", "maquina3"]


from mako.template import Template
from mako.lookup import TemplateLookup


mylookup = TemplateLookup(directories=['../templates'],
        module_directory='/tmp/mako_modules',collection_size=100,
        input_encoding='utf-8', output_encoding='utf-8',
        encoding_errors='replace')

print(mylookup.get_template('index.mako').render(m1=m1, m2=m2))
