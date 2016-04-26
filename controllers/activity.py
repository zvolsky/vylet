# -*- coding: utf-8 -*-

def list():
    return {}

def akce():
    form = SQLFORM(db.akce)
    accept(form, PP('akce byla přidána'))

    return dict(form=form)

def xupload_gpx():
    form = SQLFORM(db.trasa)
    form.insert(0, TR(LABEL('aaa'), LABEL(A(PP("Akce není v nabídce - zadat jinou/novou akci"),
                              _href=URL('akce', vars={'referrer': 'upload_gpx'}), _class="btn btn-info"))))
    accept(form, PP('trasa byla uložena'))

    return dict(form=form)

def upload_gpx():
    fields = []
    fields.append(db.akce)
    button_pos = len(fields)
    fields.append(db.trasa)
    form = SQLFORM.factory(*fields)
    form.insert(button_pos, TR(TD(LABEL('aaa')), TD(A(PP("Akce není v nabídce - zadat jinou/novou akci"),
                              _href=URL('akce', vars={'referrer': 'upload_gpx'}), _class="btn btn-info"))))
    if form.process().accepted:
        if not form.vars.client:
            id = db.akce.insert(**db.client._filter_fields(form.vars))
            form.vars.client = id
        id = db.trasa.insert(**db.address._filter_fields(form.vars))
        response.flash = PP('trasa byla uložena')
    return dict(form=form)
