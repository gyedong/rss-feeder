from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.security import verify_password, get_password_hash
from app.models.user import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def authenticate_user(db: Session, email: str, password: str):
    user = read_user_by_email(db, email)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def read_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def read_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
