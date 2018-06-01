import sys
from sqlalchemy import create_engine, MetaData

from utils import logger, config

metadata = MetaData()
metadata.schema = config['db']['schema']


def ms_sql_engine():
    try:
        db_engine = create_engine(
            "mssql+pymssql://%s:%s@%s:%s/%s" % (
                config['db']['user'],
                config['db']['password'],
                config['db']['hostname'],
                config['db']['port'],
                config['db']['database']
            )  # , echo=True
        )
        logger.info("SUCCESS: Connection to SQL Server instance succeeded")
        return db_engine
    except Exception as error:
        logger.error(
            "ERROR: Could not connect to SQL Server instance. "
            "Details: %s" % error
        )
        sys.exit()
