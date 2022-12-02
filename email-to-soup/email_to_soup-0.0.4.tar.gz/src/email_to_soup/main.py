import re
from bs4 import BeautifulSoup
from bs4 import Tag
from typing import Optional
from email.parser import Parser
from email.policy import default as default_policy
from dataclasses import dataclass

MULTIPLE_SPACES_REGEX = re.compile(r"[\s\u200c]+")

@dataclass
class EmailSoup:
    html_body: Optional[Tag]
    soup_text: str
    html_soup: BeautifulSoup

def soupify_email(email: str) -> EmailSoup:
    """Convert an email string to a BeautifulSoup object.

    Args:
        email: The email string to convert.

    Returns:
        An EmailSoup object representing the email html-soup, html-body, soup-text.
    """
    email = Parser(policy=default_policy).parsestr(email)
    html_body = email.get_body(preferencelist=('html')).get_content()
    html_soup = BeautifulSoup(html_body, features="lxml")
    email_soup = EmailSoup(
        html_soup = html_soup,
        soup_text = _extract_soup_text(html_soup),
        html_body = html_body,
    )
    return email_soup


def _extract_soup_text(html_soup: BeautifulSoup) -> str:
    try:
        return re.sub(
            MULTIPLE_SPACES_REGEX, " ", html_soup.get_text(strip=True, separator=" ")
        ).strip()
    except Exception:  # pylint: disable=broad-except
        return ""
