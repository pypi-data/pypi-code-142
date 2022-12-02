import os
import jinja2
from sendgrid.helpers.mail import (Mail, From, To, Subject, PlainTextContent,
    HtmlContent)
from tcw_tasks.templates import TEXT_TEMPLATE, HTML_TEMPLATE


class Message:
    """
    Create email message for a finished contest

    # v0.0.4, migrated to sendgrid
    """

    def __init__(self, *args, **kwargs):
        self.contest = None
        self.winners = None
        self.mail_from = os.getenv('TCW_MAIL_FROM', 'user@localhost')
        self.message = None
        self.subject = 'Your ContestKitty contest results'
        self.html = True
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

        if self.contest is None:
            raise Exception('Contest object required')


    def get_message(self):
        self.message = Mail(
            From(self.mail_from),
            To(self.contest.email),
            Subject(self.subject),
            PlainTextContent(self._get_text_msg()),
            HtmlContent(self._get_html_msg()),
        )

        return self.message


    def _get_text_msg(self):
        """
        Add plain text info to the email message
        """

        msg = jinja2.Template(TEXT_TEMPLATE).render(contest=self.contest,
            winners=self.winners)
        return msg.strip()


    def _get_html_msg(self):
        """
        Add HTML formatted text into the email message
        """

        msg = jinja2.Template(HTML_TEMPLATE).render(contest=self.contest,
            winners=self.winners)
        return msg.strip()
