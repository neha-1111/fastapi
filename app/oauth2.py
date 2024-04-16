from jose import JWTError,jwt
from datetime import datetime,timedelta
from . import schemas,database,models
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import session
from config import settings
oauth2_scheme=OAuth2PasswordBearer(tokenUrl='login')
#secret_key
#algorithm
#expiration_time
SECRET_KEY=settings.secret_key
ALGORITHM=settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES=settings.access_token_expire_minutes
def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encode_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt
def verify_access_token(token:str,credential_exceptions):
    try:
       payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
       id :str=payload.get("user_id")
       if id is None:
          raise credential_exceptions
       token_data=schemas.tokendata(id=id)
    except JWTError:
        raise credential_exceptions
    return token_data
def get_current_user(token:str=Depends(oauth2_scheme),db:session=Depends(database.get_db)):
    credentials_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"could not validate credentials",headers={"WWW-Authenticate":"Bearer"})
    token=verify_access_token(token,credentials_exception)
    user=db.query(models.user).filter(models.user.id==token.id).first()
    return user     