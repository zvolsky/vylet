# -*- coding: utf-8 -*-

from plugin_config import plucfg_allowed_structure, plucfg_allowed_global

def index():
    user_settings = db(db.plugin_config_grp.user_settings).select()
    allowed_global = plucfg_allowed_global(auth, plugins)
    global_settings = db(db.plugin_config_grp).select() if allowed_global else None
    allowed_structure = plucfg_allowed_structure(auth, plugins)
    return dict(user_settings=user_settings,
                allowed_global=allowed_global,
                global_settings=global_settings,
                allowed_structure=allowed_structure)
