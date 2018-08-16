import xmlschema
import sys


def validate(xmlfile=None, type='request'):
    """

    :type xmlfile: str
    """
    if type not in ['request', 'response', 'cixml']:
        print('Invalid xml document type')
        sys.exit()
    schema = xmlschema.XMLSchema('{}.xsd'.format(type))
    if schema.is_valid(xmlfile):
        try:
            schema.validate(xmlfile)
            return schema.is_valid(xmlfile)
        except xmlschema.XMLSchemaValidationError as e:
            raise e
