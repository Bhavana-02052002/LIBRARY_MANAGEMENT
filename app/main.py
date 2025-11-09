from app.lib.database import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.lib.tablecreationdatabase import engine,Base
from app.models import books,users
from app.routers import user,books

load_dotenv()

Base.metadata.create_all(bind=engine)


DESCRIPTION=""" Inventory Platform"""

app=FastAPI(
    description=DESCRIPTION,
    title="vm_data",
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins; modify as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods; modify as needed
    allow_headers=["*"],  # Allows all headers; modify as needed
)

# app.include_router(user.router,prefix="/register") 
# app.include_router(books.router,prefix="/books")  
app.include_router(user.router) 
app.include_router(books.router)  
#app.include_router(invget.router,prefix="/vm_details")
