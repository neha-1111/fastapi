from pydantic import BaseModel,EmailStr,conint
from pydantic_settings import BaseSettings
from datetime import datetime
from typing import Optional
class postBase(BaseModel):
    title:str
    content:str
    published:bool=True 
class postCreate(postBase):
    pass 
#response model
class userout(BaseModel):
    id:int
    email:EmailStr  
    class config:
        orm_mode=True
class post(postBase):
    id:int
    created_at:datetime
    owner_id:int
    owner:userout
    class config:
        orm_mode=True
        #to convert pydantic model to orm model 
class usercreate(BaseModel):
    id:int      
    email:EmailStr
    password:str     
class userlogin(BaseModel):
    email:EmailStr
    password:str 
class token(BaseModel):
    access_token:str
    token_type:str
class tokendata(BaseModel):
    id:Optional[str]=None     
class vote(BaseModel):
    post_id:int
    dir:conint            