# -*- coding: utf-8 -*-

def list():
    return {}

def upload_gpx():
    akce = SQLFORM(db.akce)
    accept(akce, P('akce byla přidána'))

    trasa = SQLFORM(db.trasa)
    accept(trasa, P('trasa byla uložena'))

    return dict(akce=akce, trasa=trasa)
