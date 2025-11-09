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


from os import environ
from dotenv import load_dotenv
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException
from sqlalchemy import text

load_dotenv()

DATABASE_URL = URL.create(
    drivername="mysql+aiomysql",
    username=environ.get("DB_username"),
    password=environ.get("password"),
    host=environ.get("DB_Host"),
    database=environ.get("DB_Name")
)

engine = create_async_engine(DATABASE_URL, echo=True)

async_session = sessionmaker(
    engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

async def get_async_session():
    async with async_session() as session:
        try:
            await session.execute(text("SELECT 1"))
            yield session
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"DB Error: {str(e)}")
