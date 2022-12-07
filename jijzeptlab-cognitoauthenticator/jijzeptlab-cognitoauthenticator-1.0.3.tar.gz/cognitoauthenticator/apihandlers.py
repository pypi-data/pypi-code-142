import json
from tornado import web
from jupyterhub.apihandlers.base import APIHandler
from jupyterhub.apihandlers import default_handlers

from .orm import UserInfo


class CognitoAPIHandler(APIHandler):
    async def get(self):
        user = self.current_user
        if user is None:
            raise web.HTTPError(403)
        userinfo = self.authenticator.get_user(user.name)
        get_model = self.userinfo_model
        # ensure we have permission to identify ourselves
        # all tokens can do this on this endpoint
        model = get_model(userinfo)
        self.write(json.dumps(model))

    def userinfo_model(self, userinfo):
        if isinstance(userinfo, UserInfo):
            user = userinfo
        model = {
            'kind': 'userinfo',
            'username': user.username,
            'is_authorized': user.is_authorized,
            'email' : user.email,
            'access_token': user.access_token,
            'id_token': user.id_token,
            'refresh_token': user.refresh_token
        }
        return model


default_handlers.append((r"/api/user/cognito-token", CognitoAPIHandler))
