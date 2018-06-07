from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import MultipleResultsFound

from chapters.chapter_6 import Cookie, User, Order, LineItem
from chapters.chapter_7 import session


cc_cookie = Cookie('chocolate chip', 'http://some.aweso.me/cookie/recipe.html',
                   'CC01', 12, 0.50)
# session.add(cc_cookie)
# session.commit()
# session.expunge(cc_cookie)
# insp = inspect(cc_cookie)
#
# for state in ['transient', 'pending', 'persistent', 'detached']:
#     print('{:>10}: {}'.format(state, getattr(insp, state)))

# ------------------------------------------------------------------------------

# session.add(cc_cookie)
# cc_cookie.cookie_name = 'Change chocolate chip'
# insp = inspect(cc_cookie)
#
# for attr, attr_state in insp.attrs.items():
#     if attr_state.history.has_changes():
#         print('{}: {}'.format(attr, attr_state.value))
#         print('History: {}\n'.format(attr_state.history))

# ------------------------------------------------------------------------------

# dcc = Cookie('dark chocolate chip',
#              'http://some.aweso.me/cookie/recipe_dark.html',
#              'CC02', 1, 0.75)
# session.add(dcc)
# session.commit()

# ------------------------------------------------------------------------------

# results = session.query(Cookie).one()

# try:
#     results = session.query(Cookie).one()
# except MultipleResultsFound as error:
#     print('We found too many cookies... is that even possible?')

# ------------------------------------------------------------------------------

# order = session.query(Order).first()
# session.expunge(order)
# order.line_items

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

# cookiemon = User('cookiemon', 'mon@cookie.com', '111-111-1111', 'password')
# cc = Cookie('chocolate chip', 'http://some.aweso.me/cookie/recipe.html',
#             'CC01', 12, 0.50)
#
#
# dcc = Cookie('dark chocolate chip',
#              'http://some.aweso.me/cookie/recipe_dark.html',
#              'CC02', 1, 0.75)
#
# session.add(cookiemon)
# session.add(cc)
# session.add(dcc)
#
#
# o1 = Order()
# o1.user = cookiemon
# session.add(o1)
#
# line1 = LineItem(order=o1, cookie=cc, quantity=9, extended_cost=4.50)
#
#
# session.add(line1)
# session.commit()
# o2 = Order()
# o2.user = cookiemon
# session.add(o2)
#
# line1 = LineItem(order=o2, cookie=cc, quantity=2, extended_cost=1.50)
# line2 = LineItem(order=o2, cookie=dcc, quantity=9, extended_cost=6.75)
#
#
# session.add(line1)
# session.add(line2)
# session.commit()

# ------------------------------------------------------------------------------


# def ship_it(order_id):
#     order = session.query(Order).get(order_id)
#     for li in order.line_items:
#         li.cookie.quantity = li.cookie.quantity - li.quantity
#         session.add(li.cookie)
#     order.shipped = True
#     # session.add(order)
#     session.commit()
#     print("shipped order ID: {}".format(order_id))
#
#
# # ship_it(1)
# # print(session.query(Cookie.cookie_name, Cookie.quantity).all())
#
# ship_it(2)

# ------------------------------------------------------------------------------


def ship_it(order_id):
    order = session.query(Order).get(order_id)
    for li in order.line_items:
        li.cookie.quantity = li.cookie.quantity - li.quantity
        session.add(li.cookie)
    order.shipped = True
    session.add(order)
    try:
        session.commit()
        print("shipped order ID: {}".format(order_id))
    except IntegrityError as error:
        print('ERROR: {!s}'.format(error.orig))
        session.rollback()


ship_it(2)
