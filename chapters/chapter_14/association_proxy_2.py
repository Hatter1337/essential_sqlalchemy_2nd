from chapters.chapter_14.db_ap_2 import Session, Cookie, Ingredient

session = Session()
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
# flour = Ingredient(name='Flour')
# sugar = Ingredient(name='Sugar')
# egg = Ingredient(name='Egg')
# cc = Ingredient(name='Chocolate Chips')
# cc_cookie.ingredients.extend([flour, sugar, egg, cc])
# session.add(cc_cookie)
# session.add(dcc)
# session.commit()
#
# print(cc_cookie.ingredient_names)

# ------------------------------------------------------------------------------

dcc_ingredient_list = ['Flour', 'Sugar', 'Egg', 'Dark Chocolate Chips',
                       'Oil']
existing_ingredients = session.query(Ingredient).filter(
    Ingredient.name.in_(dcc_ingredient_list)).all()
missing = set(dcc_ingredient_list) - set([x.name for x in
                                          existing_ingredients])
print(missing)
