from sqlmodel import Session, select

from etiket.app.models import (
    User,
    UserCreate,
    UserUpdate,
)
from etiket.app.crud.db import (
    get_user_from_db_by_username,
    commit_to_db,
)


class UserService:
    def __init__(self):
        pass

    async def create_user(self, user: UserCreate, session):
        db_user = User.from_orm(user)
        db_user = commit_to_db(db_user, session)
        return db_user

    async def get_users(self, offset: int, limit: int, session):
        users = session.exec(
            select(User).order_by(User.username).offset(offset).limit(limit)
        ).all()
        return users

    async def get_user(self, username: str, session):
        user = get_user_from_db_by_username(username, session)
        return user

    async def update_user(self, username: str, user: UserUpdate, session):
        db_user = get_user_from_db_by_username(username, session)
        user_data = user.dict(exclude_unset=True)
        for key, value in user_data.items():
            if value is None:
                continue
            setattr(db_user, key, value)
        db_user = commit_to_db(db_user, session)
        return db_user
