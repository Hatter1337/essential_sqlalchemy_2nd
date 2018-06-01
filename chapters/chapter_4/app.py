from chapters.chapter_4.db import dal
from sqlalchemy.sql import select

from utils import config

dal.db_init("mssql+pymssql://%s:%s@%s:%s/%s" % (
                config['db']['user'],
                config['db']['password'],
                config['db']['hostname'],
                config['db']['port'],
                config['db']['database']))


def get_orders_by_customer(cst_name, shipped=None, details=False):
    columns = [dal.orders.c.order_id, dal.users.c.username, dal.users.c.phone]
    joins = dal.users.join(dal.orders)
    if details:
        columns.extend([dal.cookies.c.cookie_name,
                        dal.line_items.c.quantity,
                        dal.line_items.c.extended_cost])
        joins = joins.join(dal.line_items).join(dal.cookies)
    cst_orders = select(columns)
    cst_orders = cst_orders.select_from(joins).where(
        dal.users.c.username == cst_name)
    if shipped is not None:
        cst_orders = cst_orders.where(dal.orders.c.shipped == shipped)
    result = dal.connection.execute(cst_orders).fetchall()
    return result


if __name__ == "__main__":
    print(get_orders_by_customer('cookiemon'))
