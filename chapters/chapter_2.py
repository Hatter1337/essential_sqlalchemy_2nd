from sqlalchemy import text, insert, update, delete, and_, or_, not_
from sqlalchemy.sql import select, func, cast

from chapters.chapter_1 import *


# ins = insert(cookies).values(
#     cookie_name="chocolate chip",
#     cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
#     cookie_sku="CC01",
#     quantity="12",
#     unit_cost="0.50"
# )

# ------------------------------------------------------------------------------

# ins = cookies.insert()
# inventory_list = [
#     {
#         'cookie_name': 'peanut butter',
#         'cookie_recipe_url': 'http://some.aweso.me/cookie/peanut.html',
#         'cookie_sku': 'PB01',
#         'quantity': '24',
#         'unit_cost': '0.25'
#     },
#     {
#         'cookie_name': 'oatmeal raisin',
#         'cookie_recipe_url': 'http://some.okay.me/cookie/raisin.html',
#         'cookie_sku': 'EWW01',
#         'quantity': '100',
#         'unit_cost': '1.00'
#     }
# ]
# result = connection.execute(ins, inventory_list)

# ------------------------------------------------------------------------------

# s = select([cookies])
# print(s)
# rp = connection.execute(s)
# results = rp.fetchall()
# print(results)
#
# first_row = results[0]
# print(first_row)
# print(first_row[1])
# print(first_row.cookie_name)
# print(first_row[cookies.c.cookie_name])
#
# rp = connection.execute(s)
# for record in rp:
#     print(record.cookie_name)

# ------------------------------------------------------------------------------

# s = select([cookies.c.cookie_name, cookies.c.quantity])
# print(s)
# rp = connection.execute(s)
# print(rp.keys())
# results = rp.first()
# print(results)

# ------------------------------------------------------------------------------

# s = select([cookies.c.cookie_name, cookies.c.quantity]) \
#     .order_by(cookies.c.quantity)
# rp = connection.execute(s)
# for cookie in rp:
#     print('{} - {}'.format(cookie.quantity, cookie.cookie_name))

# ------------------------------------------------------------------------------

# s = select([cookies.c.cookie_name, cookies.c.quantity])
# s = s.order_by(cookies.c.quantity)
# s = s.limit(2)
# rp = connection.execute(s)
# print([result.cookie_name for result in rp])

# ------------------------------------------------------------------------------

# s = select([func.sum(cookies.c.quantity)])
# rp = connection.execute(s)
# print(rp.scalar())
#
# s = select([func.count(cookies.c.cookie_name).label('inventory_count')])
# rp = connection.execute(s)
# record = rp.first()
# print(record.keys())
# print(record.inventory_count)

# ------------------------------------------------------------------------------

# s = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip')
# rp = connection.execute(s)
# record = rp.first()
# print(record.items())
#
# s = select([cookies]).where(cookies.c.cookie_name.like('%chocolate%'))
# rp = connection.execute(s)
# for record in rp.fetchall():
#     print(record.cookie_name)

# ------------------------------------------------------------------------------

# s = select([cookies.c.cookie_name,
#             cast((cookies.c.quantity * cookies.c.unit_cost),
#                  Numeric(12, 2)).label('inv_cost')])
# for row in connection.execute(s):
#     print('{} - {}'.format(row.cookie_name, row.inv_cost))

# ------------------------------------------------------------------------------

# s = select([cookies]).where(
#     and_(
#         cookies.c.quantity > 23,
#         cookies.c.unit_cost < 0.40
#     )
# )
# for row in connection.execute(s):
#     print(row.cookie_name)
#
# s = select([cookies]).where(
#     or_(
#         cookies.c.quantity.between(10, 50),
#         cookies.c.cookie_name.contains('chip')
#     )
# )
# for row in connection.execute(s):
#     print(row.cookie_name)

# ------------------------------------------------------------------------------

# u = update(cookies).where(cookies.c.cookie_name == "chocolate chip")
# u = u.values(quantity=(cookies.c.quantity + 120))
# result = connection.execute(u)
#
# print(result.rowcount)
#
# s = select([cookies]).where(cookies.c.cookie_name == "chocolate chip")
# result = connection.execute(s).first()
# for key in result.keys():
#     print('{:>20}: {}'.format(key, result[key]))

# ------------------------------------------------------------------------------

# u = delete(cookies).where(cookies.c.cookie_name == "dark chocolate chip")
# result = connection.execute(u)
# print(result.rowcount)
#
# s = select([cookies]).where(cookies.c.cookie_name == "dark chocolate chip")
# result = connection.execute(s).fetchall()
# print(len(result))

# ------------------------------------------------------------------------------

# customer_list = [
#     {
#         'username': 'cookiemon',
#         'email_address': 'mon@cookie.com',
#         'phone': '111-111-1111',
#         'password': 'password'
#     },
#     {
#         'username': 'cakeeater',
#         'email_address': 'cakeeater@cake.com',
#         'phone': '222-222-2222',
#         'password': 'password'
#     },
#     {
#         'username': 'pieguy',
#         'email_address': 'guy@pie.com',
#         'phone': '333-333-3333',
#         'password': 'password'
#     }
# ]
# ins = users.insert()
# result = connection.execute(ins, customer_list)

# ------------------------------------------------------------------------------

# ins = insert(orders).values(user_id=1, order_id=1)
# result = connection.execute(ins)
# ins = insert(line_items)
# order_items = [
#     {
#         'order_id': 1,
#         'cookie_id': 1,
#         'quantity': 2,
#         'extended_cost': 1.00
#     },
#     {
#         'order_id': 1,
#         'cookie_id': 3,
#         'quantity': 12,
#         'extended_cost': 3.00
#     }
# ]
# result = connection.execute(ins, order_items)
# ins = insert(orders).values(user_id=2, order_id=2)
# result = connection.execute(ins)
# ins = insert(line_items)
# order_items = [
#     {
#         'order_id': 2,
#         'cookie_id': 1,
#         'quantity': 24,
#         'extended_cost': 12.00
#     },
#     {
#         'order_id': 2,
#         'cookie_id': 4,
#         'quantity': 6,
#         'extended_cost': 6.00
#     }
# ]
# result = connection.execute(ins, order_items)

# ------------------------------------------------------------------------------

# columns = [orders.c.order_id, users.c.username, users.c.phone,
#            cookies.c.cookie_name, line_items.c.quantity,
#            line_items.c.extended_cost]
# cookiemon_orders = select(columns) \
#     .select_from(orders.join(users).join(line_items).join(cookies)) \
#     .where(users.c.username == 'cookiemon')
# result = connection.execute(cookiemon_orders).fetchall()
# for row in result:
#     print(row)

# ------------------------------------------------------------------------------

# columns = [users.c.username, func.count(orders.c.order_id)]
# all_orders = select(columns) \
#     .select_from(users.outerjoin(orders)) \
#     .group_by(users.c.username)
# result = connection.execute(all_orders).fetchall()
# for row in result:
#     print(row)

# ------------------------------------------------------------------------------


# def get_orders_by_customer(cust_name):
#     columns = [orders.c.order_id, users.c.username, users.c.phone,
#                cookies.c.cookie_name, line_items.c.quantity,
#                line_items.c.extended_cost]
#     cust_orders = select(columns) \
#         .select_from(users.join(orders).join(line_items).join(cookies)) \
#         .where(users.c.username == cust_name)
#     result = connection.execute(cust_orders).fetchall()
#     return result
#
#
# print(get_orders_by_customer('cakeeater'))

# ------------------------------------------------------------------------------


# def get_orders_by_customer(cust_name, shipped=None, details=False):
#     columns = [orders.c.order_id, users.c.username, users.c.phone]
#     joins = users.join(orders)
#     if details:
#         columns.extend([cookies.c.cookie_name, line_items.c.quantity,
#                        line_items.c.extended_cost])
#         joins = joins.join(line_items).join(cookies)
#     cust_orders = select(columns) \
#         .select_from(joins) \
#         .where(users.c.username == cust_name)
#     if shipped is not None:
#         cust_orders = cust_orders.where(orders.c.shipped == shipped)
#     result = connection.execute(cust_orders).fetchall()
#     return result
#
#
# print(get_orders_by_customer('cakeeater'))
#
# print(get_orders_by_customer('cakeeater', details=True))
#
# print(get_orders_by_customer('cakeeater', shipped=True))  # AttributeError
#
# print(get_orders_by_customer('cakeeater', shipped=False))  # -/-
#
# print(get_orders_by_customer('cakeeater', shipped=False, details=True))  # -/-

# ------------------------------------------------------------------------------

# result = connection.execute("select * from practice.orders").fetchall()
# print(result)

# ------------------------------------------------------------------------------

stmt = select([users]).where(text("username='cookiemon'"))
print(connection.execute(stmt).fetchall())
