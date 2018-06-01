from sqlalchemy import select, insert, update, desc
from sqlalchemy.exc import IntegrityError

from chapters.chapter_1 import *


# ins = insert(users).values(
#     username="cookiemon",
#     email_address="mon@cookie.com",
#     phone="111-111-1111",
#     password="password"
# )
# result = connection.execute(ins)
#
# s = select([users.c.username])
# results = connection.execute(s)
# for result in results:
#     print(result.username)
#     print(result.password)

# ------------------------------------------------------------------------------

# s = select([users.c.username])
# connection.execute(s).fetchall()
#
# ins = insert(users).values(
#     username="cookiemon",
#     email_address="damon@cookie.com",
#     phone="111-111-1111",
#     password="password"
# )
# result = connection.execute(ins)

# ------------------------------------------------------------------------------

# ins = insert(users).values(
#     username="cookiemon",
#     email_address="damon@cookie.com",
#     phone="111-111-1111",
#     password="password"
# )
# try:
#     result = connection.execute(ins)
# except IntegrityError as error:
#     print(str(error))
#     print(error.params)

# ------------------------------------------------------------------------------

# ins = cookies.insert()
# inventory_list = [
#     {
#         'cookie_name': 'chocolate chip',
#         'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe.html',
#         'cookie_sku': 'CC01',
#         'quantity': '12',
#         'unit_cost': '0.50'
#     },
#     {
#         'cookie_name': 'dark chocolate chip',
#         'cookie_recipe_url': 'http://some.aweso.me/cookie/recipe_dark.html',
#         'cookie_sku': 'CC02',
#         'quantity': '1',
#         'unit_cost': '0.75'
#     }
# ]
# result = connection.execute(ins, inventory_list)

# ------------------------------------------------------------------------------

# ins = insert(orders).values(user_id=1, order_id='1')
# result = connection.execute(ins)
# ins = insert(line_items)
# order_items = [
#     {
#         'order_id': 1,
#         'cookie_id': 1,
#         'quantity': 9,
#         'extended_cost': 4.50
#     }
# ]
# result = connection.execute(ins, order_items)
#
# ins = insert(orders).values(user_id=1, order_id='2')
# result = connection.execute(ins)
# ins = insert(line_items)
# order_items = [
#     {
#         'order_id': 2,
#         'cookie_id': 1,
#         'quantity': 4,
#         'extended_cost': 1.50
#     },
#     {
#         'order_id': 2,
#         'cookie_id': 2,
#         'quantity': 1,
#         'extended_cost': 4.50
#     }
# ]
# result = connection.execute(ins, order_items)

# ------------------------------------------------------------------------------


# def ship_it(order_id):
#     s = select([line_items.c.cookie_id, line_items.c.quantity]) \
#         .where(line_items.c.order_id == order_id)\
#         .order_by(desc(line_items.c.cookie_id))
#     cookies_to_ship = connection.execute(s).fetchall()
#
#     for cookie in cookies_to_ship:
#         print("Cookie: %s" % cookie)
#         u = update(cookies).where(cookies.c.cookie_id == cookie.cookie_id) \
#             .values(quantity=cookies.c.quantity - cookie.quantity)
#         connection.execute(u)
#
#     u = update(orders).where(orders.c.order_id == order_id) \
#         .values(shipped=True)
#     connection.execute(u)
#     print("Shipped order ID: {}".format(order_id))
#
#
# # ---
#
# # ship_it(1)
# # s_ = select([cookies.c.cookie_name, cookies.c.quantity])
# # connection.execute(s_).fetchall()
#
# # ---
#
# ship_it(2)

# ------------------------------------------------------------------------------


def ship_it(order_id):
    s = select([line_items.c.cookie_id, line_items.c.quantity]) \
        .where(line_items.c.order_id == order_id)
    transaction = connection.begin()
    cookies_to_ship = connection.execute(s).fetchall()

    try:
        for cookie in cookies_to_ship:
            u = update(cookies).where(cookies.c.cookie_id == cookie.cookie_id) \
                .values(quantity=cookies.c.quantity-cookie.quantity)
            connection.execute(u)

        u = update(orders).where(orders.c.order_id == order_id)
        u = u.values(shipped=True)
        connection.execute(u)

        print("Shipped order ID: {}".format(order_id))
        transaction.commit()
    except IntegrityError as error:
        transaction.rollback()
        print(error)


ship_it(2)
