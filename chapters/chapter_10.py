from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from utils import config

Base = automap_base()
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


Base.prepare(engine, reflect=True)
print(Base.classes.keys())

# ------------------------------------------------------------------------------

artist = Base.classes.artist
album = Base.classes.album

session = Session(engine)
for art in session.query(artist).limit(10):
    print(art.artist_id, art.name)

# ------------------------------------------------------------------------------

art = session.query(artist).first()
for alb in art.album_collection:
    print('{} - {}'.format(art.name, alb.title))
