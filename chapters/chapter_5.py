from sqlalchemy import MetaData, Table, create_engine, select

from utils import config

metadata = MetaData()
metadata.schema = config['db']['schema']
engine = create_engine(
    "mssql+pymssql://%s:%s@%s:%s/%s" % (
        config['db']['user'],
        config['db']['password'],
        config['db']['hostname'],
        config['db']['port'],
        config['db']['database']
    )
)

# artist = Table('artist', metadata, autoload=True, autoload_with=engine)
# album = Table('album', metadata, autoload=True, autoload_with=engine)

# s = select([artist]).limit(10)
# print(engine.execute(s).fetchall())
#
# s = select([album]).limit(10)
# print(engine.execute(s).fetchall())

# print(metadata.tables)
# print(album.foreign_keys)
# print(str(artist.join(album)))

# ------------------------------------------------------------------------------

metadata.reflect(bind=engine)
# print(metadata.tables.keys())

artist = metadata.tables['practice.artist']
album = metadata.tables['practice.album']

s = select([artist.c.name, album.c.title]).select_from(artist.join(album))
print(engine.execute(s).fetchall())
