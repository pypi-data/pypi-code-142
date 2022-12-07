from datetime import datetime, timedelta
from typing import Optional
from sqlmodel import Session, select
from sqlalchemy.exc import NoResultFound
from fastapi import Depends, HTTPException, status, Form, Path
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from etiket.app.crud.db import get_session
from etiket.app.models import User, Token
from etiket.core.utils import *
from etiket.core.config import settings
from etiket.core.exceptions import *


SECRET_KEY = settings.ETIKET_SECRET_KEY
ALGORITHM = "HS256"  # env variable

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/token")


def verify_password(
    plain_password,
    hashed_password,
):

    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(
    username: str,
    password: str,
    session: Session = Depends(get_session),
):

    try:
        user = session.exec(select(User).where(User.username == username)).one()
    except NoResultFound:
        return False

    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False

    return user


def create_token(
    data: dict,
    expires_delta: Optional[timedelta] = None,
):

    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def get_access_refresh_tokens(username: str) -> Token:

    access_token_expires = get_access_token_expiration_time()
    access_token = create_token(
        data={"sub": username, "type": "access"}, expires_delta=access_token_expires
    )

    refresh_token_expires = get_refresh_token_expiration_time()
    refresh_token = create_token(
        data={"sub": username, "type": "refresh"}, expires_delta=refresh_token_expires
    )

    token = Token(access_token=access_token, refresh_token=refresh_token)

    return token


def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session),
):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        token_type: str = payload.get("type")
        if username is None:
            raise ValidationCredentialsException
        if token_type != "access":
            raise ValidationCredentialsException
    except JWTError:
        raise ValidationCredentialsException
    except jwt.JWTClaimsError:
        raise ValidationCredentialsException
    except jwt.ExpiredSignatureError:
        raise ValidationCredentialsException

    try:
        user = session.exec(select(User).where(User.username == username)).one()
    except NoResultFound:
        raise ValidationCredentialsException
    if user is None:
        raise ValidationCredentialsException

    return user


def get_refreshed_user(
    token: str = Depends(oauth2_scheme),
    grant_type: str = Form(..., regex="refresh_token"),
    refresh_token: str = Form(...),
    session: Session = Depends(get_session),
):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_username: str = payload.get("sub")
        token_type: str = payload.get("type")
        if token_username is None:
            raise ValidationCredentialsException
        if token_type != "access":
            raise RefreshTokenException
        # Should not reach this part if not expired
        raise NonExpiredRefreshTokenException

    except jwt.ExpiredSignatureError:
        # only if the access token is expired --> decode the refresh token
        try:
            accessclaims = jwt.get_unverified_claims(token)
            token_username: str = accessclaims.get("sub")
            token_type: str = accessclaims.get("type")
            if token_username is None:
                raise RefreshTokenException
            if token_type != "access":
                raise RefreshTokenException

            payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
            refresh_username: str = payload.get("sub")
            refresh_token_type: str = payload.get("type")
            if refresh_username is None:
                raise RefreshTokenException
            if refresh_username != token_username:
                raise RefreshTokenException
            if refresh_token_type != "refresh":
                raise RefreshTokenException
        except jwt.ExpiredSignatureError:
            raise InvalidRefreshTokenException
        except jwt.JWTClaimsError:
            raise RefreshTokenException
        except JWTError:
            raise RefreshTokenException

    except JWTError:
        raise RefreshTokenException
    except jwt.JWTClaimsError:
        raise InvalidRefreshTokenException

    if refresh_username is None:
        raise InvalidRefreshTokenException
    try:
        user = session.exec(select(User).where(User.username == refresh_username)).one()
    except NoResultFound:
        raise ValidationCredentialsException
    if user is None:
        raise ValidationCredentialsException

    return user


def get_current_active_user(
    current_user: User = Depends(get_current_user),
):

    if current_user.active:
        return current_user

    raise InactiveUserException


def get_refreshed_active_user(
    current_user: User = Depends(get_refreshed_user),
):

    if current_user.active:
        return current_user

    raise InactiveUserException


def get_current_active_adminuser(
    current_adminuser: User = Depends(get_current_active_user),
):

    if not current_adminuser.admin:
        raise AdminUserException

    return current_adminuser
