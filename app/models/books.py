from sqlalchemy import Column,Integer,String,Boolean,DateTime
from datetime import datetime
from app.lib.tablecreationdatabase import Base

class Books(Base):
    __tablename__="books"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(200),nullable=False)
    author=Column(String(150),nullable=False)
    published_year=Column(Integer)
    available=Column(Boolean,default=True)
    created_at=Column(DateTime,default=datetime.utcnow)







