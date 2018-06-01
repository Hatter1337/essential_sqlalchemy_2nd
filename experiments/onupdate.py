from datetime import datetime
from sqlalchemy.orm import sessionmaker, mapper
from sqlalchemy import Table, Column, Integer, String, DateTime

from db import ms_sql_engine, metadata
from utils import *


now = datetime.utcnow().strftime(config['date']['format'])

posts = Table(
    'posts', metadata,
    Column('post_id', Integer(), primary_key=True),
    Column('text', String(200)),
    Column('create_time', DateTime(), default=now),
    Column('last_modified_time', DateTime(), default=now, onupdate=now)
)

# metadata.create_all(engine)


class Posts(object):
    def __init__(self, text):
        self.text = text
        self.create_time = None
        self.last_modified_time = None

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (
            self.text, self.create_time, self.last_modified_time)


mapper(Posts, posts)

engine = ms_sql_engine()
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

try:
    # new_post = Posts('Hello!')
    post = session.query(Posts).filter(Posts.post_id == 3).first()
    post.text = 'Hi, again!'
    session.add(post)
    session.commit()
except Exception as error:
    print(error)
finally:
    session.close()
