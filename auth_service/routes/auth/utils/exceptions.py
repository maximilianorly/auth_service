class AuthorizationHeaderMissing(Exception):
    pass

class InvalidToken(Exception):
    pass

class JWTDecodeError(Exception):
    pass

class TokenExpirationError(Exception):
    pass

class TokenBlacklistError(Exception):
    pass