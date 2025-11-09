from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlmodel import select
from app.routers.user import SECRET_KEY, ALGORITHM
from app.schema.books import BookCreate, Bookupadte
from app.models.books import Books
from app.lib.database import get_async_session, AsyncSession

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return email  
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

@router.post("/api/books")
async def add_book(book: BookCreate,session: AsyncSession = Depends(get_async_session),current_user: str = Depends(get_current_user)):
    try:
        new_book = Books(**book.dict())
        session.add(new_book)
        await session.commit()
        await session.refresh(new_book)
        return {"message": "Book added successfully"} 
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=f"Error adding book: {str(e)}")


@router.get("/api/books/{id}")
async def get_book(id: int,session: AsyncSession = Depends(get_async_session),current_user: str = Depends(get_current_user)):
    try:
        result = await session.execute(select(Books).where(Books.id == id))
        book = result.scalars().first()
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        return book
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving book: {str(e)}")


@router.get("/api/books")
async def get_books(session: AsyncSession = Depends(get_async_session),current_user: str = Depends(get_current_user)):
    try:
        result = await session.execute(select(Books))
        books = result.scalars().all()
        if not books:
            raise HTTPException(status_code=404, detail="No books found")
        return books
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving books: {str(e)}")


@router.delete("/api/books/{id}")
async def delete_book(id: int,session: AsyncSession = Depends(get_async_session),current_user: str = Depends(get_current_user)):
    try:
        result = await session.execute(select(Books).where(Books.id == id))
        book = result.scalars().first()
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        await session.delete(book)
        await session.commit()
        return {"message": "Book deleted successfully"}
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting book: {str(e)}")


@router.put("/api/books/{id}")
async def update_book(id: int,book_update: Bookupadte,session: AsyncSession = Depends(get_async_session),current_user: str = Depends(get_current_user)):
    try:
        result = await session.execute(select(Books).where(Books.id == id))
        book = result.scalars().first()
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
        for key, value in book_update.dict(exclude_unset=True).items():
            setattr(book, key, value)
        session.add(book)
        await session.commit()
        await session.refresh(book)
        return {"message": "Book updated successfully"}
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating book: {str(e)}")
