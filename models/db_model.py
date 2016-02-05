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

db.define_table('poradani',
    Field('poradatel_id', db.auth_user, label=P("Akce"),
          comment=P('Porádaná akce')),
    Field('akce_id', db.akce, label=P("Akce"),
          comment=P('Porádaná akce')),
    format='%(poradatel_id)s - %(akce_id)s'
    )

db.define_table('znamy',
    Field('auth_user_id', db.auth_user, default=auth.user_id, label=P("Uživatel"),
          comment=P('vlastník tohoto kontaktu')),
    Field('profil_id', db.auth_user, label=P("Profil známého"),
          comment=P('uživatelský profil známého, pokud je evidován a rozpoznán'),
          requires=IS_EMPTY_OR(IS_IN_DB(db, db.auth_user.id, lambda r: r.username)),
          represent=lambda f, row: f and P("existuje") or P("není znám")),
    Field('nick', length=32, label=P("Přezdívka"),
          comment=P('přezdívka účastníka')),
    Field('email', length=64, label=P("eMail"),
          comment=P('emailová adresa')),
    Field('ode_dne', 'date', label=P("Ode dne"),
          comment=P('chcete-li, můžete uvést první účast na vaší akci (i třeba neevidované na tomto webu)')),
    Field('autoimport', 'date', label=P("Auto-importován"),
          comment=P('byl přidán autoomaticky z došlé pošty'),
          represent=lambda f, row: f and P("ano") or ''),
    Field('blokovan', 'boolean', label=P("Blokován(a)"),
          comment=P('zablokuje veškerou poštu mezi vámi (zprostředkovanou tímto webem)')),
    format='%(nick)s'
    )

db.define_table('mailer',
    Field('auth_user_id', db.auth_user, default=auth.user_id, label=P("Uživatel"),
          comment=P('vlastník této konfigurace')),
    Field('smtp', length=64, label=P("Odesílaná pošta (SMTP)"),
          comment=P('zadejte, jestliže chcete rozesílat pozvánky pomocí tohoto systému')),
    Field('email', length=64, default=db.auth_user.email, label=P("eMail"),
          comment=P('odesílat pod emailovou adresou (ve většině případů vaše obvyklá adresa)')),
    format='%(nick)s'
    )

db.define_table('mail_in',
    Field('auth_user_id', db.auth_user, default=auth.user_id, label=P("Uživatel"),
          comment=P('vlastník této konfigurace')),
    Field('znamy_id', db.znamy, label=P("Známý"),
          comment=P('známý, od nějž chci sledovat poštu a hledat v ní akce a galerie')),
    Field('imap', length=64, label=P("Došlá pošta (IMAP)"),
          comment=P('adresa (IMAP) pro automatické hledání informací v došlé poště (např. imap.google.com)')),
    Field('slozka', length=96, label=P("Složka"),
          comment=P('ve které složce chcete hledat e-maily známé(ho)')),
    Field('aktivni', 'boolean', default=True, label=P("Povoleno"),
          comment=P('označte položku, pokud se má opravdu v současné době používat')),
    format='%(imap)s - %(složka)s'
    )

db.define_table('typ_galerie',
    Field('typ', length=32, label=P("Typ galerie")),
    format='%(typ)s'
    )

db.define_table('galerie',
    Field('akce_id', db.akce, label=P("Akce"),
          comment=P('akce, k níž se vztahuje tato galerie')),
    Field('typ_galerie_id', db.typ_galerie, label=P("Typ galerie")),
    Field('profil_id', db.auth_user, label=P("Autor galerie"),
          comment=P('autor galerie, pokud má profil a podaří se jej přiřadit')),
    Field('odkaz', length=192, label=P("Adresa galerie"),
          comment=P('odkaz, URL galerie')),
    format='%(odkaz)s'
    )

db.define_table('fotozdroj',
    Field('auth_user_id', db.auth_user, default=auth.user_id, label=P("Uživatel"),
          comment=P('vlastník této informace')),
    Field('galerie_id', db.akce, label=P("Akce"),
          comment=P('akce, k níž se vztahuje tato galerie')),
    Field('znamy_id', db.znamy, label=P("Známý"),
          comment=P('vyberte známého(známou, který(á) zveřejnil(a) tento odkaz')),
    Field('autoimport', 'date', label=P("Auto-importován"),
          comment=P('byl přidán autoomaticky z došlé pošty')),
    format='%(odkaz)s'
    )
