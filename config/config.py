import logging
import os

# TODO Create proper logging.
# TODO Create proper testing.
# TODO Create folder structure
def logger(default_level='INFO', file='logs.log'):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(file)
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger

SCHEMAS_FOLDER = '{}\\schema\\'.format(os.getcwd())

DATABASE_CONFIG = {
    'host': 'localhost',
    'port' : 27017,
    'database' : 'curri',
}
