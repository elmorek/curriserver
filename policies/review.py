from config.db import getdb

db = getdb()
collection = db.policies

def getpolicies(data):
    policies = []
    for key, value in data.items():
        if data[key] is not None:
            newpolicies = collection.find({'if.{}.{}'.format(key, 'value') : value })
            for policy in newpolicies:
                policies.append(policy)
    #TODO Remove duplicates
    return policies


