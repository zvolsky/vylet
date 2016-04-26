# -*- coding: utf-8 -*-

from gluon import *

def PP(txt):
    return txt  # dummy messages translation

def link(*files):
    for file in files:
        if not '.' in file:
            file = '%s.%s' % (file, file.split('/', 1)[0])
    current.response.files.append(URL('static', file))

def accept(form, ok_msg=PP('záznam byl uložen')):
    """zpracování formuláře s defaultní, explicitní nebo žádnou(None) hláškou po uložení"""
    if form.process().accepted:
        if ok_msg:
            current.response.flash = ok_msg
        if current.request.vars.referrer:
            redirect(URL(current.request.vars.referrer))
    elif form.errors:
        current.response.flash = PP('prosím, oprav chyby')
