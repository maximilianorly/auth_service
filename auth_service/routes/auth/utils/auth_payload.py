import os
import datetime

class auth_payload(dict):

    def __init__(self, id, clientId, isAdmin):
        EXPIRESSECONDS = int(os.getenv('EXPIRESSECONDS'))

        self["id"] = id
        self["sub"] = clientId
        self["isAdmin"] = isAdmin
        self["exp"] = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(seconds=EXPIRESSECONDS)).isoformat()