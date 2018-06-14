from sqlalchemy import Column, Integer, Numeric, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
from sqlalchemy.orm import sessionmaker
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
    __tablename__ = 'cookies'

    cookie_id = Column(Integer, primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))

    @property
    def inventory_value(self):
        return self.unit_cost * self.quantity

    @hybrid_method
    def bake_more(self, min_quantity):
        return self.quantity < min_quantity

    def __repr__(self):
        return "Cookie(cookie_name='{self.cookie_name}', " \
            "cookie_recipe_url='{self.cookie_recipe_url}', " \
            "cookie_sku='{self.cookie_sku}', " \
            "quantity={self.quantity}, " \
            "unit_cost={self.unit_cost})".format(self=self)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
