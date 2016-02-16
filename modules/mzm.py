# -*- coding: utf-8 -*-

from gluon import *

def P(txt):
    return txt  # dummy messages translation

def link(*files):
    for file in files:
        if not '.' in file:
            file = '%s.%s' % (file, file.split('/', 1)[0])
    current.response.files.append(URL('static', file))

def accept(form, ok_msg=P('záznam byl uložen')):
    """zpracování formuláře s defaultní, explicitní nebo žádnou(None) hláškou po uložení"""
    if form.process().accepted:
        if ok_msg:
            response.flash = ok_msg
    elif form.errors:
        response.flash = m.P('prosím, oprav chyby')
