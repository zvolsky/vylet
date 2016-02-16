# -*- coding: utf-8 -*-

import datetime

from mzm import P, accept, link
link('js/mz/mzj', 'css/mz/mzc')

## if SSL/HTTPS is properly configured and you want all HTTP requests to
## be redirected to HTTPS, uncomment the line below:
if request.is_local:
    from gluon.custom_import import track_changes
    track_changes(True)    # auto-reload modules
#else:
#    request.requires_https()
