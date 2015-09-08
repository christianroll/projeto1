#!/usr/bin/env python
# -*-*- encoding: utf-8 -*-*-
# Created: Tue, 08 Sep 2015 03:49:46 -0300

from mako.template import Template
from mako.lookup import TemplateLookup


mylookup = TemplateLookup(directories=['../templates'],
                    module_directory='/tmp/mako_modules',
                    collection_size=100,
                    input_encoding='utf-8',
                    output_encoding='utf-8',
                    encoding_errors='replace')

def serve_template(templatename, **kwargs):
    mytemplate = mylookup.get_template(templatename)
    print(mytemplate.render(**kwargs))
