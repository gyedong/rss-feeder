from typing import Any

from fastapi import APIRouter, Depends

from app.api.depends import get_current_active_user
from app.models.user import User
from app.schemas.user import UserRead

router = APIRouter()


@router.get("/me", response_model=UserRead, response_model_exclude={'password'})
def read_user_me(current_user: User = Depends(get_current_active_user)) -> UserRead:
    return current_user
