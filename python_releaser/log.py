import logging
import logging.config
import sys

logging.config.dictConfig(dict(
    version=1,
    formatters={
        'cli_out': {
            'format': '%(message)s',
        },
    },
    handlers={
        'cli': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'cli_out',
            'level': 'DEBUG',
        }
    },
    loggers={
        __name__: {
            'level': 'INFO',
            'handlers': ['cli'],
        }
    }
))

logger = logging.getLogger(__name__)


def get_pad(level):
    pad = ''
    if level > 0:
        pad = ('  ' * level) + '└─ '
    return pad


def fatal(msg, l=0):
    logger.fatal(get_pad(l) + 'error: ' + msg)
    sys.exit(1)


def debug(msg, l=0):
    logger.debug(get_pad(l) + '[debug] ' + msg)


def dry(name, msg, l=0):
    logger.info(get_pad(l) + '[warn] dry-run ({}): '.format(name) + msg)


def write(msg, l=0):
    logger.info(get_pad(l) + msg)


def write_and_exit(msg, l=0):
    logger.info(get_pad(l) + msg)
    sys.exit(0)
