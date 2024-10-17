from fastapi import APIRouter
from tinydb import TinyDB, Query
from fastapi import FastAPI, HTTPException
import uvicorn
from DataBase import Student, StudentTable
api_router = APIRouter()
from random import randint

@api_router.get("/insert_rand")
def get_student():
    rand = randint(1,999)
    StudentTable.insert({'dig': rand})
    return {'dig': rand}
    
@api_router.get("/view_all")
def get_student():
    return StudentTable.all()

@api_router.get('/hello')
def hello():
    return {'hello'}