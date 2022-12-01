from lxml import html
import requests
import weblogin
import weblogin.seamlessaccess as sa
import urllib.parse

class SSOlogin(weblogin.AutologinHandler):
  """
  Login handler (weblogin.AutologinHandler) for LADOK logins.
  """
  LOGIN_URL = "https://www.start.ladok.se/gui/loggain"
  
  def __init__(self,
      institution,
      login_trigger_url="https://www.start.ladok.se/gui/"):
    """
    Creates a login handler that automates the LADOK part of authentication.
    - Requires `institution`. A string identifying the instutution at 
      SeamlessAccess.org.
    - Optional `login_trigger_url` is a page that redirects to the login page,
      for instance, the API URLs don't redirect, but the UI URLs do.

    This login handler must be used in conjunction with a university login 
    handler.
    """
    super().__init__()
    self.__institution = institution
    self.__login_trigger_url = login_trigger_url
    self.__logging_in = False

  def need_login(self, response):
    """
    Checks a response to determine if logging in is needed,
    returns True if needed
    """
    if self.__logging_in:
      return False
    elif response.status_code == requests.codes.unauthorized \
         and "ladok.se" in response.url:
      return True
    elif response.url.find(self.LOGIN_URL) == 0:
      return True

    return False

  def login(self, session, response, args=None, kwargs=None):
    """
    Performs a login based on the response `response` from a request to session 
    `session`.
    `args` and `kwargs` are the options from the request triggering the login 
    procedure, this is so that we can redo that request after logging in.

    Raises an AuthenticationError exception if authentication fails.
    """
    self.__logging_in = True
    response = session.get("https://www.start.ladok.se/Shibboleth.sso/Login"
                           "?target=https://www.start.ladok.se/gui/shiblogin")
    parsed_url = urllib.parse.urlparse(response.url, allow_fragments=False)
    if "seamlessaccess.org" not in parsed_url.netloc:
      raise weblogin.AuthenticationError(
                      f"seamlessaccess.org not in {parsed_url.netloc}")

    return_url = urllib.parse.unquote(
                            urllib.parse.parse_qs(parsed_url.query)["return"][0])
    if "{sha1}" in self.__institution:
      entityID = sa.get_entity_data_by_id(self.__institution)["entityID"]
    else:
      entityID = sa.find_entity_data_by_name(self.__institution)[0]["entityID"]
    if "?" in return_url:
      return_url += f"&entityID={entityID}"
    else:
      return_url += f"?entityID={entityID}"

    ladok_response = session.get(return_url)
    self.__logging_in = False

    if args and response.history:
      return session.request(*args, **kwargs)
    return ladok_response
