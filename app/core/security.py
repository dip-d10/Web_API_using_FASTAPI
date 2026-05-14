from datetime import datetime, timezone, timedelta
from jose import Jwt, JWTError
from app.core.config import settings


def create_token(data: dict, expire_minutes = 30):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes = expire_minutes)
    to_encode.update({'exp' : expire})
    return Jwt.encode(
        settings.JWT_SECRET_KEY,
        algorithms  = settings.JWT_ALGORITHM        
    )
   
    
def verify_token(token: str):
    try:
        payload = Jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms = [settings.JWT_ALGORITHM]    
        )
        return payload
    except JWTError:
        return None  