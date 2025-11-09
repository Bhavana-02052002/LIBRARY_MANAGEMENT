from fastapi import APIRouter, Depends, HTTPException
from app.schema.users import UserCreate, loginrequest
from app.lib.database import get_async_session  # use async session
from sqlmodel import select
from app.models.users import Users as User
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

SECRET_KEY = "MYSECRETKEY"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


@router.post("/api/register")
async def register_user(user: UserCreate, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(User).where(User.email == user.email))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=409, detail="Email already registered")
    hashed_pw = hash_password(user.password)
    new_user = User(name=user.name, email=user.email, password=hashed_pw)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    
    return {"message": "User was created successfully"}

@router.post("/api/login")
async def login_user(login_data: loginrequest, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(User).where(User.email == login_data.email))
    user = result.scalars().first()
    
    if not user or not verify_password(login_data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    
    payload = {
        "sub": user.email,
        "exp": datetime.utcnow() + timedelta(hours=1)
    }
    
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    
    return {"access_token": token, "token_type": "bearer"}


