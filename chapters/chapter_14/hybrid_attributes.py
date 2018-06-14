from sqlalchemy import desc

from chapters.chapter_14.db import Session, Cookie

session = Session()


# print(Cookie.inventory_value < 10.00)
# print(Cookie.bake_more(12))

# ------------------------------------------------------------------------------

# cc_cookie = Cookie(cookie_name='chocolate chip',
#                    cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
#                    cookie_sku='CC01',
#                    quantity=12,
#                    unit_cost=0.50)
# dcc = Cookie(cookie_name='dark chocolate chip',
#              cookie_recipe_url='http://some.aweso.me/cookie/recipe_dark.html',
#              cookie_sku='CC02',
#              quantity=1,
#              unit_cost=0.75)
# mol = Cookie(cookie_name='molasses',
#              cookie_recipe_url='http://some.aweso.me/cookie/'
#                                'recipe_molasses.html',
#              cookie_sku='MOL01',
#              quantity=1,
#              unit_cost=0.80)
# session.add(cc_cookie)
# session.add(dcc)
# session.add(mol)
# session.flush()
#
# print(dcc.inventory_value)
# print(dcc.bake_more(12))

# ------------------------------------------------------------------------------

for cookie in session.query(Cookie).order_by(desc(Cookie.inventory_value)):
    print('{:>20} - {:.2f}'.format(cookie.cookie_name, cookie.inventory_value))

# ------------------------------------------------------------------------------

for cookie in session.query(Cookie).filter(Cookie.bake_more(12)):
    print('{:>20} - {}'.format(cookie.cookie_name, cookie.quantity))
