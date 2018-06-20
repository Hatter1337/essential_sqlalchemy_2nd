from sqlalchemy import (Column, Integer, Numeric, String, Table,
                        ForeignKey, create_engine)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
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

Session = sessionmaker(bind=engine)


cookieingredients_table = Table('cookieingredients', Base.metadata,
    Column('cookie_id', Integer, ForeignKey("cookies.cookie_id"),
           primary_key=True),
    Column('ingredient_id', Integer, ForeignKey("ingredients.ingredient_id"),
           primary_key=True)
)


class Ingredient(Base):
    __tablename__ = 'ingredients'

    ingredient_id = Column(Integer, primary_key=True)
    name = Column(String(255), index=True)

    def __repr__(self):
        return "Ingredient(name='{self.name}')".format(self=self)


class Cookie(Base):
    __tablename__ = 'cookies'

    cookie_id = Column(Integer, primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))

    ingredients = relationship("Ingredient",
                                secondary=cookieingredients_table)

    def __repr__(self):
        return "Cookie(cookie_name='{self.cookie_name}', " \
                       "cookie_recipe_url='{self.cookie_recipe_url}', " \
                       "cookie_sku='{self.cookie_sku}', " \
                       "quantity={self.quantity}, " \
                       "unit_cost={self.unit_cost})".format(self=self)


Base.metadata.create_all(engine)
