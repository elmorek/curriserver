from schema.schema import validate
from messageprocess.request import todict
import xml.etree.ElementTree as ET
from config.config import logger
import falcon

class CURRIServer():

    def __init__(self):
        self.log = logger('INFO', 'logs.log')

    def on_post(self, req, resp):
        headers = req.headers
        assert isinstance(req.headers, dict)
        reqheaders = {
            'User-Agent' : 'CiscoUCM-HttpClient/1.0',
            'methodName' : 'isRoleAccessAllowed',
        }
        for key in headers in reqheaders.keys():
            if headers[key] != reqheaders[key]:
                resp.status = falcon.HTTP_400
                resp.body = 'Invalid headers'
                self.log.error('Invalid header {}. Expected value: {}'.format(key, reqheaders[key]))

        if req.body:
            assert isinstance(req.body, str)
            request = ET.fromstring(req.body)
            if not validate(req.body, 'request'):
                resp.status = falcon.HTTP_400
                resp.body = 'Request not valid'
                self.log.error('Invalid request. Body must be compliant with CURRI XACML schema')
            request = todict(request)
