import os
import jinja2
from email.message import EmailMessage
from tcw_tasks.templates import TEXT_TEMPLATE, HTML_TEMPLATE


class Message:
    """
    Create email message for a finished contest
    """

    def __init__(self, *args, **kwargs):
        self.contest = None
        self.winners = None
        self.mail_from = os.getenv('TCW_MAIL_FROM', 'user@localhost')
        self.message = None
        self.subject = 'Your contest results'
        self.html = True
        for k, v in kwargs.items():
            if hasattr(self, k):
                setattr(self, k, v)

        if self.contest is None:
            raise Exception('Contest object required')


    def get_message(self):
        self.message = EmailMessage()
        self.message['From'] = self.mail_from
        self.message['To'] = self.contest.email
        self.message['Subject'] = self.subject

        self._add_text_msg()
        if self.html is True:
            self._add_html_msg()

        return self.message


    def _add_text_msg(self):
        """
        Add plain text info to the email message
        """

        msg = jinja2.Template(TEXT_TEMPLATE).render(contest=self.contest,
            winners=self.winners)
        self.message.set_content(msg.strip())


    def _add_html_msg(self):
        """
        Add HTML formatted text into the email message
        """

        msg = jinja2.Template(HTML_TEMPLATE).render(contest=self.contest,
            winners=self.winners)
        self.message.add_alternative(msg.strip())
