from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.security import create_access_token
from app.crud.auth import create_user
from app.crud.auth import read_user_by_email, authenticate_user
from app.db.session import Base, engine, get_db
from app.schemas.user import UserCreate

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.post("/register")
def post(user: UserCreate, db: Session = Depends(get_db)):
    db_user = read_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)


@router.post("/login/access-token")
async def login_for_access_token(user: UserCreate, db: Session = Depends(get_db)):
    user = authenticate_user(db, user.email, user.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(subject=user.email, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
