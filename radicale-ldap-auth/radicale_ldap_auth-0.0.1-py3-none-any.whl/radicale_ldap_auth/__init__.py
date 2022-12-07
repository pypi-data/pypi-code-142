from radicale.auth import BaseAuth
# from radicale.log import logger
import ldap

PLUGIN_CONFIG_SCHEMA = {
    "auth": {
    "ldap_url": {"value": "", "type": str},
    "ldap_port": {"value": "", "type": str},
    "ldap_user_postfix": {"value": "", "type": str}
        }
    }


class Auth(BaseAuth):
    def __init__(self, configuration):
        super().__init__(configuration.copy(PLUGIN_CONFIG_SCHEMA))

    def login(self, user, password):
        config_url = self.configuration.get("auth", "ldap_url")
        config_port = self.configuration.get("auth", "ldap_port")
        ldap_user_postfix = self.configuration.get("auth", "ldap_user_postfix")

        ldap_url = f'{config_url}:{config_port}'
        # logger.info("user attempt by %r with password %r",
        #             user, password, ldap_url, ldap_user_postfix)
        l = ldap.initialize(ldap_url)
        l.set_option(ldap.OPT_REFERRALS, 0)
        while True:
            try:
                l.simple_bind_s(user, password)
                break
            except ldap.INVALID_CREDENTIALS as error:
                if not '@' in user:
                    user = f'{user}@{ldap_user_postfix}'
                else:    
                    return ""
        l.unbind_s()
        return user.split('@')[0]
