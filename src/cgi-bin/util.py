#!/usr/bin/env python2
# -*-*- encoding: utf-8 -*-*-
# Created: Sun, 04 Oct 2015 08:02:40 -0300

"""
Useful tools
"""


from __future__ import division
from __future__ import print_function


__authors__ = (
    'Christian Rollmann',
    'Isaac Mitsuaki Saito',
    'Julio Batista Silva',
    'Marcelo Fernandes Tedeschi',)
__license__ = "GPL v3"
__version__ = "1.0"


comandos = [
            {'num': '1', 'nome': 'ps'},
            {'num': '2', 'nome': 'df'},
            {'num': '3', 'nome': 'finger'},
            {'num': '4', 'nome': 'uptime'},
           ]


# Get command name from it's number
def cmd_name(cmd):
    return{
       '1': 'ps',
       '2': 'df',
       '3': 'finger',
       '4': 'uptime'
    }.get(cmd, '')  # TODO:raise exception if invalid cmd


# Returns a list with all localhost IPs. Needs netifaces
def get_host_ip():
    from netifaces import interfaces, ifaddresses, AF_INET
    ip_list = []
    for interface in interfaces():
        if interface in ['lo', 'lo0']:
            continue
        for link in ifaddresses(interface).get(AF_INET, ()):
            ip_list.append(link['addr'])
    return ip_list
