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


def fatal(msg, *args, **kwargs):
    logger.fatal('error: ' + msg, *args, **kwargs)
    sys.exit(1)


def debug(msg, *args, **kwargs):
    logger.debug('[debug] ' + msg, *args, **kwargs)


def dry(msg, *args, **kwargs):
    logger.info('[warn] dry-run: ' + msg, *args, **kwargs)


def write(msg, *args, **kwargs):
    logger.info(msg, *args, **kwargs)


def write_and_exit(msg, *args, **kwargs):
    logger.info(msg, *args, **kwargs)
    sys.exit(0)
