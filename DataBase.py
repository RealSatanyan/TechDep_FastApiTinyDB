from pydantic import BaseModel, Field
from tinydb import TinyDB, Query

class Student(BaseModel):
    id: int = Field(default=None, alias='_id')
    dig: int


db = TinyDB('db.json')
StudentTable = db.table('Student')

