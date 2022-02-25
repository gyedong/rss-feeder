from sqlalchemy import Boolean, Column, String
from sqlalchemy.dialects.mysql import INTEGER
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(INTEGER(display_width=11, unsigned=True), primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    is_active = Column(Boolean, default=True)
