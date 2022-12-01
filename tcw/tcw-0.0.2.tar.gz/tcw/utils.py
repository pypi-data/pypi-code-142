import string
import secrets
import datetime
import markdown
from sqlalchemy import func, or_, and_
from .database import session
from tcw.apps.contest.models import Contest, Entrant


def contest_by_name(name):
    contest = session.query(Contest).filter(Contest.name == name).one()
    if not contest:
        raise Exception("No contest with name %s" % name)

    return contest


def expired_contests():
    now = datetime.datetime.utcnow()
    subq = session.query(
        func.count(Contest.entrants) >= Contest.max_entrants).scalar_subquery()

    contests = session.query(Contest).filter(
        or_(Contest.expires < now, subq )
    ).all()

    if not contests:
        raise Exception("No contests that meet criteria")

    return contests


def random_name(length=24):
    """
    create random name for contests. a mix of alphanum chars.

    args:
        - int name length
    returns:
        - str
    """

    letters = string.ascii_letters
    digits = string.digits
    alphabet = letters + digits
    name = ''

    while len(name) < length:
        name += secrets.choice(alphabet)

    return name


def expires_time(hours=1.0):
    """
    get a datetime object x number of hours in the future.

    args:
        - float hours into the future
    returns:
        - datateime object, None on  error
    """

    later = None
    try:
        now = datetime.datetime.utcnow().replace(second=0, microsecond=0)
        later = now + datetime.timedelta(hours=hours)
    except:
        pass

    return later


def md_to_html(txt):
    """
    Convert markdown text to HTML.

    args:
        - str (markdown text)
    returns:
        str (html text)
    """

    try:
        html = markdown.markdown(txt)
        return html
    except:
        return txt
