from chapters.chapter_9.db import Cookie, LineItem, Order, User,  dal


def get_orders_by_customer(cst_name, shipped=None, details=False):
    query = dal.session.query(Order.order_id, User.username, User.phone)
    query = query.join(User)
    if details:
        query = query.add_columns(Cookie.cookie_name, LineItem.quantity,
                                  LineItem.extended_cost)
        query = query.join(LineItem).join(Cookie)
    if shipped is not None:
        query = query.filter(Order.shipped == shipped)
    results = query.filter(User.username == cst_name).all()
    return results


if __name__ == "__main__":
    dal.connect()
    dal.session = dal.Session()
    print(get_orders_by_customer('cookiemon'))
    dal.session.close()
