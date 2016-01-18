# -*- coding: utf-8 -*-

import datetime

def P(txt):
    return txt  # dummy messages translation

## app configuration made easy. Look inside private/appconfig.ini
from gluon.contrib.appconfig import AppConfig
## once in production, remove reload=True to gain full speed
myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    ## if NOT running on Google App Engine use SQLite or other DB
    db = DAL(myconf.take('db.uri'), pool_size=myconf.take('db.pool_size', cast=int), check_reserved=['all'])
else:
    ## connect to Google BigTable (optional 'google:datastore://namespace')
    db = DAL('google:datastore+ndb')
    ## store sessions and tickets there
    session.connect(request, response, db=db)
    ## or store session in Memcache, Redis, etc.
    ## from gluon.contrib.memdb import MEMDB
    ## from google.appengine.api.memcache import Client
    ## session.connect(request, response, db = MEMDB(Client()))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []
## choose a style for forms
response.formstyle = myconf.take('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.take('forms.separator')


## (optional) optimize handling of static files
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'
## (optional) static assets folder versioning
# response.static_version = '0.0.0'
#########################################################################
## Here is sample code if you need for
## - email capabilities
## - authentication (registration, login, logout, ... )
## - authorization (role based authorization)
## - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
## - old style crud actions
## (more options discussed in gluon/tools.py)
#########################################################################

from gluon.tools import Auth, Service, PluginManager

auth = Auth(db)
service = Service()
plugins = PluginManager()

auth.settings.create_user_groups = None
auth.settings.extra_fields['auth_user'] = [
    Field('email_ver', 'boolean', default=True, label=P("Mail není tajný"),
          comment=P('zaškrtni, pokud chceš dovolit zobrazování Tvé e-mailové adresy na stránkách')),
    Field('telefon', length=50, default='', label=P("Telefon"),
          comment=P('pro organizátora vždy doporučujeme vyplnit (i když nemusí být zveřejněn)')),
    Field('tel_ver', 'boolean', default=True, label=P("Tel. není tajný"),
          comment=P('zaškrtni, pokud chceš dovolit zobrazování Tvého telefonního čísla na stránkách')),
    Field('organizator', 'boolean', default=False,
          label=P('Organizátor akcí'),
          comment=P('chci mít k dispozici více voleb pro organizování akcí')),
    Field('ode_dne', 'date', readable=False, writable=False,
        default=datetime.date.today(), label=P('Ode dne'),
        comment=P('registrován od...')),
    Field('prihlasen', 'date', label=P('Přihlášen'), readable=False, writable=False,
        comment=P('naposledy přihlášen dne')),
    Field('neposilat', 'boolean', default=False, label=P('Neposílat pozvánky'),
        comment=P('neposílat pozvánky od kteréhokoli organizátora (chci je sledovat jen na webu')),
    ]

## create all tables needed by auth if not custom tables
auth.define_tables(username=True, signature=False)
db.auth_user.username.comment = P('přihlašovací jméno a zároveň přezdívka, zobrazovaná ostatním')

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' if request.is_local else myconf.take('smtp.server')
mail.settings.sender = myconf.take('smtp.sender')
mail.settings.login = myconf.take('smtp.login')

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

#########################################################################
## Define your tables below (or better in another model file) for example
##
## >>> db.define_table('mytable',Field('myfield','string'))
##
## Fields can be 'string','text','password','integer','double','boolean'
##       'date','time','datetime','blob','upload', 'reference TABLENAME'
## There is an implicit 'id integer autoincrement' field
## Consult manual for more options, validators, etc.
##
## More API examples for controllers:
##
## >>> db.mytable.insert(myfield='value')
## >>> rows=db(db.mytable.myfield=='value').select(db.mytable.ALL)
## >>> for row in rows: print row.id, row.myfield
#########################################################################

## after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)
