# -*- coding: utf-8 -*-

db.define_table('akce',
    Field('auth_user_id', db.auth_user, default=auth.user_id, label=PP("Zapsal uživatel"),
          writable=False, readable=False,
          comment=PP('kdo založil tento záznam o akci')),
    Field('nazev', length=30, label=PP("Název akce"),
          comment=PP('Název akce (případně stručná trasa výletu, apod.')),
    Field('sraz', 'datetime', label=PP("Sraz"),
          comment=PP('čas srazu')),
    Field('sraziste', length=128, label=PP("Místo srazu"),
          comment=PP('místo srazu')),
    Field('zacatek', 'datetime', label=PP("Začátek"),
          comment=PP('čas začátku nebo odjezdu')),
    Field('kam', length=256, label=PP("O odjezdu"),
          comment=PP('více informací k odjezdu (směr vlaku, nástupiště, kde lze přistoupit)')),
    Field('ukonceni', 'datetime', label=PP("Předpokládané ukončení"),
          comment=PP('předpokládané ukončení nebo návrat')),
    Field('popis', 'text', label=PP("Popis"),
          comment=PP('podrobnosti akce nebo pozvánky')),
    format='%(nazev)s'
    )

db.define_table('trasa',
    Field('akce_id', db.akce, label=PP("Akce"),
          comment=PP('akce, k níž se vztahuje tato trasa')),
    Field('auth_user_id', db.auth_user, default=auth.user_id, label=PP("Přidal uživatel"),
          writable=False, readable=False,
          comment=PP('kdo nahrál tuto trasu')),
    Field('typ', 'integer', requires=IS_IN_SET([('N', PP('návrh')), ('G', PP('stopa GPS')), ('P', PP('přibližný zpětný zákres'))],
                                                zero='', error_message=PP('zvol jednu z možností')),
          label=PP("Typ záznamu trasy"), comment=PP('N návrh, G GPS stopa, P přibližný zpětný zákres')),
    Field('trasa', 'upload', label=PP("Gpx soubor"),
          comment=PP('trasa výletu nebo cesty ve formátu gpx (záznam GPS, mapy.cz-Měření/Plánování-Exportovat, ..)')),
    Field('datum', 'date', label=PP("Datum trasy"),
          comment=PP('datum (pro přiřazení k akci, apod.)')),
    Field('poznamka', 'text', label=PP("Poznámka"),
          comment=PP('část cesty nebo varianta, možná porucha GPS záznamu, apod.')),
    format='%(nazev)s'
    )

db.define_table('poradani',
    Field('poradatel_id', db.auth_user, label=PP("Akce"),
          comment=PP('Porádaná akce')),
    Field('akce_id', db.akce, label=PP("Akce"),
          comment=PP('Pořádaná akce')),
    format='%(poradatel_id)s - %(akce_id)s'
    )

db.define_table('znamy',
    Field('auth_user_id', db.auth_user, default=auth.user_id, label=PP("Uživatel"),
          comment=PP('vlastník tohoto kontaktu')),
    Field('profil_id', db.auth_user, label=PP("Profil známého"),
          comment=PP('uživatelský profil známého, pokud je evidován a rozpoznán'),
          requires=IS_EMPTY_OR(IS_IN_DB(db, db.auth_user.id, lambda r: r.username)),
          represent=lambda f, row: f and PP("existuje") or PP("není znám")),
    Field('nick', length=32, label=PP("Přezdívka"),
          comment=PP('přezdívka účastníka')),
    Field('email', length=64, label=PP("eMail"),
          comment=PP('emailová adresa')),
    Field('ode_dne', 'date', label=PP("Ode dne"),
          comment=PP('chcete-li, můžete uvést první účast na vaší akci (i třeba neevidované na tomto webu)')),
    Field('autoimport', 'date', label=PP("Auto-importován"),
          comment=PP('byl přidán autoomaticky z došlé pošty'),
          represent=lambda f, row: f and PP("ano") or ''),
    Field('blokovan', 'boolean', label=PP("Blokován(a)"),
          comment=PP('zablokuje veškerou poštu mezi vámi (zprostředkovanou tímto webem)')),
    format='%(nick)s'
    )

db.define_table('mailer',
    Field('auth_user_id', db.auth_user, default=auth.user_id, label=PP("Uživatel"),
          comment=PP('vlastník této konfigurace')),
    Field('smtp', length=64, label=PP("Odesílaná pošta (SMTP)"),
          comment=PP('zadejte, jestliže chcete rozesílat pozvánky pomocí tohoto systému')),
    Field('email', length=64, default=db.auth_user.email, label=PP("eMail"),
          comment=PP('odesílat pod emailovou adresou (ve většině případů vaše obvyklá adresa)')),
    format='%(nick)s'
    )

db.define_table('mail_in',
    Field('auth_user_id', db.auth_user, default=auth.user_id, label=PP("Uživatel"),
          comment=PP('vlastník této konfigurace')),
    Field('znamy_id', db.znamy, label=PP("Známý"),
          comment=PP('známý, od nějž chci sledovat poštu a hledat v ní akce a galerie')),
    Field('imap', length=64, label=PP("Došlá pošta (IMAP)"),
          comment=PP('adresa (IMAP) pro automatické hledání informací v došlé poště (např. imap.google.com)')),
    Field('slozka', length=96, label=PP("Složka"),
          comment=PP('ve které složce chcete hledat e-maily známé(ho)')),
    Field('aktivni', 'boolean', default=True, label=PP("Povoleno"),
          comment=PP('označte položku, pokud se má opravdu v současné době používat')),
    format='%(imap)s - %(složka)s'
    )

db.define_table('typ_galerie',
    Field('typ', length=32, label=PP("Typ galerie")),
    format='%(typ)s'
    )

db.define_table('galerie',
    Field('akce_id', db.akce, label=PP("Akce"),
          comment=PP('akce, k níž se vztahuje tato galerie')),
    Field('typ_galerie_id', db.typ_galerie, label=PP("Typ galerie")),
    Field('profil_id', db.auth_user, label=PP("Autor galerie"),
          comment=PP('autor galerie, pokud má profil a podaří se jej přiřadit')),
    Field('odkaz', length=192, label=PP("Adresa galerie"),
          comment=PP('odkaz, URL galerie')),
    format='%(odkaz)s'
    )

db.define_table('fotozdroj',
    Field('auth_user_id', db.auth_user, default=auth.user_id, label=PP("Uživatel"),
          comment=PP('vlastník této informace')),
    Field('galerie_id', db.akce, label=PP("Akce"),
          comment=PP('akce, k níž se vztahuje tato galerie')),
    Field('znamy_id', db.znamy, label=PP("Známý"),
          comment=PP('vyberte známého(známou, který(á) zveřejnil(a) tento odkaz')),
    Field('autoimport', 'date', label=PP("Auto-importován"),
          comment=PP('byl přidán autoomaticky z došlé pošty')),
    format='%(odkaz)s'
    )
