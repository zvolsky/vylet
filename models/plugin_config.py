# -*- coding: utf-8 -*-

# Web2py plugin to manage/save/load config items.
# Items saved as single 'group' with 'item's can be loaded into single python dictionary with keys 'item's.

db.define_table('plugin_config_grp',
    Field('grp', length=16),
    Field('user_settings', 'boolean'),
    Field('txt_label', length=92),
    Field('txt_comment', 'text'),
    format='%(grp)s'
    )

db.define_table('plugin_config_key',
    Field('plugin_config_grp_id', db.plugin_config_grp),
    Field('dict_key', length=16),
    Field('txt_label', length=92),
    Field('txt_comment', 'text'),
    format='%(dict_key)s'
    )

db.define_table('plugin_config_val',
    Field('plugin_config_key_id', db.plugin_config_key),
    Field('auth_user_id', db.auth_user),
    Field('dict_value', length=256),
    format='%(dict_value)s'
    )

# Following cofiguration values are defaults.
# You can change them in db.py or other model (alphabetically after db.py, but before this model).
# Example: to disable rights to do changes for the admin group members, set: plugins.config.admin_group=''

def _():
    from gluon.tools import PluginManager
    plugins = PluginManager('config',
            admin_group='admin',  # name of the admin group (all changes allowed for members). empty string to disable
                                  # in addition changes are enabled for members of following groups:
                                  #     plugin_config_structure - change configuration structure
                                  #     plugin_config_global - change global settings
                                  #   everybody can change his/her own setting
            )

plugin_manage_groups = _()
