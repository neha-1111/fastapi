from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import sys
from . import models,auth
from .database import engine
from .routers import user,post,vote
from .config import settings
from . import env
models.base.metadata.create_all(bind=engine)
app=FastAPI()  
origins=['*'] #we can send our api request from any domain
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# while True:    
#     try:
#         conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='9899281089',cursor_factory=RealDictCursor)
#         cursor=conn.cursor()
#         print('database connection was successfull')
#         break
#     except Exception as error:
#         print('connecting to database failed')
#         print('Error:',error) 
#         time.sleep(2)   
# my_posts=[{"title":"title of post1","content":"content of post 1","id":1},
#           {"title":"title of post 2","content":"i like pizza","id":2}]
# def find_posts(id):
#     for p in my_posts:
#         if p['id']==id:
#             return p
app.include_router(post.router)
app.include_router(user.router)  
app.include_router(auth.router)  
app.include_router(vote.router)    
@app.get('/')
async def root():
    return {'message':'Hello World'}


     


