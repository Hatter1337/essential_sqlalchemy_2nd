import logging
import logging.config


class SingleLineFormatter(logging.Formatter):
    """
    Logging formatter to display the message on one line. Used to reformat
    database queries to be on one line so log file filtering gets the whole
    line.
    """
    def format(self, record):
        """Returns record with new lines stripped."""
        message = super(SingleLineFormatter, self).format(record)
        message = message.replace('\n', ' ')
        return ' '.join(message.split())


def setup_logging():
    default_format = '%(asctime)s %(levelname)s %(message)s'

    settings = {
        'version': 1,
        'formatters': {
            'default': {
                'format': default_format
            },
            'singleline': {
                '()': 'utils.log.SingleLineFormatter',
                'format': default_format
            }
        },
        'handlers': {
            'practice': {
                'formatter': 'default',
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout'
            },
            'db': {
                'formatter': 'singleline',
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout'
            }
        },
        'loggers': {
            'practice': {
                'handlers': ['practice'],
                'propagate': False,
                'level': 'INFO'
            },
            'urllib3': {
                'handlers': ['practice'],
                'propagate': False,
                'level': 'DEBUG'
            },
            'sqlalchemy.engine': {
                'handlers': ['db'],
                'propagate': False,
                'level': 'INFO'
            }
        },
        'root': {
            'handlers': ['practice'],
            'level': 'INFO'
        }
    }

    logging.config.dictConfig(settings)

    return logging.getLogger('practice')
