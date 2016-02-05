# -*- coding: utf-8 -*-

def plucfg_allowed_structure(auth, plugins):
    """is user allowed to change the configuration structure (definitions)
    """
    return auth.has_membership('plugin_config_structure') or plucfg_is_admin(auth, plugins)

def plucfg_allowed_global(auth, plugins):
    """is user allowed to set the global configuration (the default for all users)
    """
    return auth.has_membership('plugin_config_global') or plucfg_is_admin(auth, plugins)

def plucfg_is_admin(auth, plugins):
    return plugins.config.admin_group and auth.has_membership(plugins.config.admin_group)
