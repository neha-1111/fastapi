from fastapi import FastAPI,responses,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import session
from ..database import get_db
from .. import models,utils,schemas,oauth2
router=APIRouter(
    prefix="/posts",
    tags=['posts']
    )
@router.get("/")
def get_posts(db:session=Depends(get_db)):
    posts=db.query(models.post).all()
    return {"data":posts}
 #regular method using standard sql   
#    try:
#        cursor.execute("select * from posts")
#        posts=cursor.fetchall()
#        return {"data":posts}
#    except Exception as error:
#        return {"error":str(error)}

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.post)
def create_post(post:schemas.postCreate,db:session=Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    #   cursor.execute('''insert into posts (title,content,published) values(%s,%s,%s) returning *''',(post.title,post.content,post.published))
    #   new_post=cursor.fetchone()
    #   conn.commit()
    new_Post=models.post(owner_id=current_user.id,**post.dict())
    db.add(new_Post)
    db.refresh(new_Post)
    return {'data':new_Post}
# def find_index_post(id:int):
#     for i,p in enumerate(my_posts):
#         if p['id']==id:
#             return i
# @router.get("/posts/{id}")
# def get_post(id:int):
#     # cursor.execute('''select * from posts where id=%s''',str(id))
#     # post=cursor.fetchone()
#     # if not post:
#     #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with {id} is not found')
#     #     # response.status_code=status.HTTP_404_NOT_FOUND
#     #     # return{'message':f'post with {id} is not found'}
#     # return {"post_detail":post}
# @router.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id:int):
#     cursor.execute('''delete from posts where id =%s returning *''',str(id))
#     deleted_post=cursor.fetchone()
#     conn.commit()
#     if not delete_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'this index is not present')  
#     return Response(status_code=status.HTTP_204_NO_CONTENT)
# @router.put('/posts/{id}')
# def update_posts(id:int,post:schemas.post):
#     cursor.execute('''update posts set title=%s,content=%s,published=%s where id=%s returning *''',(post.title,post.content,post.published,str(id)) )
#     updated_post=cursor.fetchone()
#     conn.commit()
#     if not updated_post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'this index is not present')  
#     return{"data":updated_post}