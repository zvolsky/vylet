# -*- coding: utf-8 -*-

@auth.requires_login()
def index():
    response.view = 'global_/grid.html'
    return dict(hdr=PP("Zadejte známé, které např. chcete zvát na akce nebo z jejichž mailů si chcete evidovat akce a galerie k akcím."),
                grid=_grid(db.znamy, db.znamy.nick))

def _grid(query, orderby):
    grid = SQLFORM.grid(
        query,
        deletable=True,
        editable=True,
        create=True,
        csv=True,
        showbuttontext=False,
        # maxtextlengths={'auth_user.email' : 30},
        paginate=100,
        searchable=False,
        orderby=orderby,
        )
    return grid
