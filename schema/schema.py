import xmlschema
import sys
import os
from config.config import SCHEMAS_FOLDER


def validate(xmlfile=None, type='request'):
    """

    :type xmlfile: str
    """
    if type not in ['request', 'response', 'cixml']:
        print('Invalid xml document type')
        sys.exit()
    else:
        schema = xmlschema.XMLSchema('{}{}.xsd'.format(SCHEMAS_FOLDER, type))
        return schema.is_valid(xmlfile)

