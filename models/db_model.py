# -*- coding: utf-8 -*-

db.define_table('akce',
    Field('nazev', length=30, label=P("Název akce"),
          comment=P('Název akce (případně stručná trasa výletu, apod.')),
    Field('sraz', 'datetime', label=P("Sraz"),
          comment=P('čas srazu')),
    Field('sraziste', length=128, label=P("Místo srazu"),
          comment=P('místo srazu')),
    Field('zacatek', 'datetime', label=P("Začátek"),
          comment=P('čas začátku nebo odjezdu')),
    Field('kam', length=256, label=P("O odjezdu"),
          comment=P('více informací k odjezdu (směr vlaku, nástupiště, kde lze přistoupit)')),
    Field('ukonceni', 'datetime', label=P("Předpokládané ukončení"),
          comment=P('předpokládané ukončení nebo návrat')),
    Field('popis', 'text', label=P("Popis"),
          comment=P('podrobnosti akce / pozvánky')),
    format='%(nazev)s'
    )
