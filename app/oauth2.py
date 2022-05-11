from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from . import schema, database, models
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings



oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


SECRET_KEY = settings.secret_key
ALGORITHM = 'HS256' 
ACCESS_TOKEN_EXPIRES_MINUTES = settings.access_token_expire_minutes


def create_access_token(data:dict):
    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRES_MINUTES)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def varify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        id = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = schema.TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_scheme),db:Session= Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f'Could not validate credentials', headers={'www-Authenticate': 'Bearer'})



    token = varify_access_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user