from auth_service.routes.auth.utils.exceptions import TokenBlacklistError
from .store import redis_client

def blacklist_token(token, exp):
    try:
        # Set the token in Redis with an extended (5 mins) expiration time over JWT exp
        redis_client.setex(token, exp + 300, "blacklisted")
        
        return True, "Token blacklisted successfully"
    except Exception as error:
        print(f"Error blacklisting token: {error}")
        raise TokenBlacklistError("Error blacklisting token")

def is_token_blacklisted(token):
    try:
        if redis_client.get(token):
            return True, "Token blacklisted"
        return False
    except Exception as error:
        print(error)
        raise TokenBlacklistError("Error checking blacklist status") 