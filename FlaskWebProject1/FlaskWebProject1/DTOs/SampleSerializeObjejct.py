from json import JSONEncoder

import json

class MobilePhone:

    contacts = None

    apps     = None

   

    def __init__(self, contacts, apps):

        self.contacts   = contacts

        self.apps       = apps

   

    def startCall():

        pass

 

    def endCall():

        pass

class MobilePhoneEncoder(JSONEncoder):

    def default(self, object):

        if isinstance(object, MobilePhone):

            return object.__dict__

        else:

            # call base class implementation which takes care of

            # raising exceptions for unsupported types

            return json.JSONEncoder.default(self, object)
