from sqlalchemy import create_engine, Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

from utils import config

Base = declarative_base()
Base.metadata.schema = config['db']['schema']
engine = create_engine(
    "mssql+pymssql://%s:%s@%s:%s/%s" % (
        config['db']['user'],
        config['db']['password'],
        config['db']['hostname'],
        config['db']['port'],
        config['db']['database']
    )
)


class Cookie(Base):
    __tablename__ = 'new_cookies'

    cookie_id = Column(Integer, primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))
