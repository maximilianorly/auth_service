class auth_response(dict):

    def __init__(self, token, expiresin, isAdmin):
        self["token"] = token
        self["expiresin"] = expiresin
        self["isAdmin"] = isAdmin
