#!/usr/bin/env python2
# -*-*- encoding: utf-8 -*-*-
# Created: Sun, 04 Oct 2015 03:46:31 -0300

"""
Just one function from a library with some useful networking tools
"""


__author__ = "Julio Batista Silva"
__copyright__ = "Copyright (c) 2015, Julio Batista Silva"
__license__ = "LGPL v3.0"
__version__ = "1.0"
__email__ = "julio@juliobs.com"


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
