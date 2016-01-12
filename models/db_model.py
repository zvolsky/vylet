# -*- coding: utf-8 -*-

db.define_table('akce',
    Field('nazev', length=30, label=p("Název akce"),
          comment=p('Název akce (případně stručná trasa výletu, apod.')),
    Field('sraz', 'datetime', label=p("Sraz"),
          comment=p('čas srazu')),
    Field('sraziste', length=128, label=p("Místo srazu"),
          comment=p('místo srazu')),
    Field('zacatek', 'datetime', label=p("Začátek"),
          comment=p('čas začátku nebo odjezdu')),
    Field('kam', length=256, label=p("O odjezdu"),
          comment=p('více informací k odjezdu (směr vlaku, nástupiště, kde lze přistoupit)')),
    Field('ukonceni', 'datetime', label=p("Předpokládané ukončení"),
          comment=p('předpokládané ukončení nebo návrat')),
    Field('popis', 'text', label=p("Popis"),
          comment=p('podrobnosti akce / pozvánky')),
    format='%(nazev)s'
    )
