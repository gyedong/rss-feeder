from typing import Any

from fastapi import APIRouter, Depends

from app.api.depends import get_current_active_user
from app.models.user import User

router = APIRouter()


@router.get("/me")
def read_user_me(current_user: User = Depends(get_current_active_user)) -> Any:
    return current_user
