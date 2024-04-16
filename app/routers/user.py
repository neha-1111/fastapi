from fastapi import FastAPI,responses,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import session
from .. import models,utils,schemas,oauth2
from ..database import get_db
router=APIRouter(
    prefix="/users",
    tags=['users']
)
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.userout)
def create_user(user:schemas.usercreate,db:session=Depends(get_db),get_current_user:int=Depends(oauth2.get_current_user)):
    hashed_password=utils.hash(user.password)
    user.password=hashed_password
    new_user=models.user(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
@router.get("/{id}",response_model=schemas.userout)
def get_user(id:int,user:schemas.usercreate,db:session=Depends(get_db)):
     hashed_password=utils.hash(user.password)
     user.password=hashed_password
     user=db.query(models.user).filter(models.user.id==id).first()
     if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'this is not present')
     return{"data":user}