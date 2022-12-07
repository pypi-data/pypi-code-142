from sqlmodel import Session, select

from etiket.app.models import (
    Scope,
    ScopeCreate,
    ScopeUpdate,
)
from etiket.app.crud.db import (
    commit_to_db,
    get_scope_from_db_by_name,
    get_user_from_db_by_username,
)
from etiket.core.exceptions import (
    UserNotInScopeException,
    UserNotFoundException,
    UserAlreadyPartOfScopeException,
)


class ScopeService:
    def __init__(self):
        pass

    async def create_scope(self, scope: ScopeCreate, session):
        db_scope = Scope.from_orm(scope)
        db_scope = commit_to_db(db_scope, session)
        return db_scope

    async def get_scopes(self, name: str, offset: int, limit: int, session):
        stmt = select(Scope)
        if name is not None:
            stmt = stmt.where(Scope.name.like(name + "%"))
        scopes = session.exec(
            stmt.order_by(Scope.name).offset(offset).limit(limit)
        ).all()
        return scopes

    async def get_scope(self, name: str, session):
        db_scope = get_scope_from_db_by_name(name, session)
        return db_scope

    async def update_scope(self, name: str, scope: ScopeUpdate, session):
        db_scope = get_scope_from_db_by_name(name, session)
        scope_data = scope.dict(exclude_unset=True)
        for key, value in scope_data.items():
            if value is None:
                continue
            setattr(db_scope, key, value)
        db_scope = commit_to_db(db_scope, session)
        return db_scope

    async def add_user_to_scope(self, scope: str, username: str, user, session):
        db_scope = get_scope_from_db_by_name(scope, session)
        if not user.admin:
            if user not in db_scope.users:
                raise UserNotInScopeException(scope)
        adduser = get_user_from_db_by_username(username, session)
        if adduser is None:
            raise UserNotFoundException(username)
        if adduser in db_scope.users:
            raise UserAlreadyPartOfScopeException(username, scope)
        db_scope.users.append(adduser)
        db_scope = commit_to_db(db_scope, session)
        return db_scope

    async def remove_user_from_scope(self, scope: str, username: str, session):
        db_scope = get_scope_from_db_by_name(scope, session)
        deluser = get_user_from_db_by_username(username, session)
        if deluser is None:
            raise UserNotFoundException(username)
        if deluser not in db_scope.users:
            raise UserAlreadyNotPartOfScopeException(username, scope)
        db_scope.users.remove(deluser)
        db_scope = commit_to_db(db_scope, session)
        return db_scope
