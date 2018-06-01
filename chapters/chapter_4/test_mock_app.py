import mock
import unittest
from decimal import Decimal

from chapters.chapter_4.app import get_orders_by_customer


class TestApp(unittest.TestCase):
    cookie_orders = [(u'wlk001', u'cookiemon', u'111-111-1111')]
    cookie_details = [
        (u'wlk001', u'cookiemon', u'111-111-1111',
            u'dark chocolate chip', 2, Decimal('1.00')),
        (u'wlk001', u'cookiemon', u'111-111-1111',
            u'oatmeal raisin', 12, Decimal('3.00'))]

    @mock.patch('chapters.chapter_4.app.select')
    @mock.patch('chapters.chapter_4.app.dal.connection')
    def test_orders_by_customer_blank(self, mock_conn, mock_select):
        mock_select.return_value \
            .select_from.return_value.where.return_value = None
        mock_conn.execute.return_value.fetchall.return_value = []
        results = get_orders_by_customer('')
        self.assertEqual(results, [])

    @mock.patch('chapters.chapter_4.app.dal.connection')
    def test_orders_by_customer_blank_shipped(self, mock_conn):
        mock_conn.execute.return_value.fetchall.return_value = []
        results = get_orders_by_customer('', True)
        self.assertEqual(results, [])

    @mock.patch('chapters.chapter_4.app.dal.connection')
    def test_orders_by_customer(self, mock_conn):
        mock_conn.execute.return_value.fetchall \
            .return_value = self.cookie_orders
        results = get_orders_by_customer('cookiemon')
        self.assertEqual(results, self.cookie_orders)
