from sqlmodel import Session

from etiket.app.models import (
    Token,
)
from etiket.core.security import (
    authenticate_user,
    get_access_refresh_tokens,
)
from etiket.core.exceptions import (
    IncorrectUsernamePasswordException,
)


class TokenService:
    def __init__(self):
        pass

    async def get_tokens(self, form_data, session: Session):
        user = authenticate_user(form_data.username, form_data.password, session)
        if not user:
            raise IncorrectUsernamePasswordException
        token = get_access_refresh_tokens(user.username)
        return token

    async def refresh_tokens(self, username):
        token = get_access_refresh_tokens(username)
        return token
