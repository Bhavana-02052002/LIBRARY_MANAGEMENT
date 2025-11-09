from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from os import environ
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base

load_dotenv()

Base=declarative_base()


db_url_object=URL.create(
     username=environ.get("DB_username"),
     drivername="mysql+pymysql",
     password=environ.get("password"),
     host=environ.get("DB_Host"),
     database=environ.get("DB_Name")
)

engine=create_engine(url=db_url_object)





# from os import environ
# from dotenv import load_dotenv
# from sqlalchemy.engine.url import URL
# from sqlmodel import Session,create_engine
# from fastapi import HTTPException
# from sqlalchemy import text
# from sqlalchemy.orm import declarative_base

# Base=declarative_base()

# load_dotenv()

# db_url_object=URL.create(
#      username=environ.get("DB_username"),
#      drivername="mysql+pymysql",
#      password=environ.get("password"),
#      host=environ.get("DB_Host"),
#      database=environ.get("DB_Name")
# )

# engine=create_engine(url=db_url_object)

# def get_session():
#     try:
#         session = Session(engine)
#         # test connection
#         session.execute(text("SELECT 1"))
#         yield session
#     except Exception as e:
#         raise HTTPException(
#             status_code=500,
#             detail=f"Unexpected database error: {str(e)}"
#         )
#     finally:
#             session.close()