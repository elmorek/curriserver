from xml.etree import ElementTree as ET
from io import BytesIO
from messageprocess.request import todict
from config.config import logger
from policies.review import getpolicies
import falcon

class RouteRequest():

    def __init__(self):
        # TODO Fix logging
        self.log = logger('DEBUG', 'logs.log')
        self.reqheaders = {
            'User-Agent' : 'CiscoUCM-HttpClient/1.0',
            'methodName' : 'isRoleAccessAllowed',
        }

    def on_post(self, req, resp):
        for header, value in self.reqheaders.items():
            if self.reqheaders[header] != req.get_header(name=header, required=True):
                self.log.error('Bad Request, expected header {} with value {}. Got {}'.format(header, value, req.get_header(name=header)), exc_info=True)
                resp.status = falcon.HTTP_400
                resp.body = 'Bad Request, expected header {} with value {}. Got {}'.format(header, value, req.get_header(name=header))

        if resp.status is not falcon.HTTP_400:
            data = req.bounded_stream.read().decode('utf-8')
            if data is None:
                resp.status = falcon.HTTP_400
                self.log.error('Request does not include data')
            else:
                #resp.content_type = falcon.MEDIA_JSON
                # TODO Add XML declaration with BytesIO
                data = todict(data)
                policies = getpolicies(data)
                print(policies)
                resp.body = str(policies)

api = application = falcon.API()
api.add_route('/request', RouteRequest())