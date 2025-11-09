from pydantic import BaseModel,EmailStr
from datetime import datetime

class BookCreate(BaseModel):
    title:str
    author:str 
    published_year:int
    available:bool=True
    
class Bookupadte(BaseModel):
    title:str=None
    author:str=None 
    published_year:int=None
    available:bool=True