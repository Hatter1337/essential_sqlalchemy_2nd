"""Renaming cookies to new_cookies

Revision ID: 86d238fe8323
Revises: 6d212e6c24ff
Create Date: 2018-06-12 11:23:46.664466

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86d238fe8323'
down_revision = '6d212e6c24ff'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('cookies', 'new_cookies', schema='practice')


def downgrade():
    op.rename_table('new_cookies', 'cookies', schema='practice')
