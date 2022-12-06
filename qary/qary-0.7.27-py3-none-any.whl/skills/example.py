""" Pattern and template based chatbot dialog engines """
import logging

from qary.skills.base import normalize_replies, ContextBaseSkill


log = logging.getLogger('qary')

# engine = Engine()


class Skill(ContextBaseSkill):
    r""" Skill that can reply with answers to frequently asked questions using data/faq/*.yml

    >>> bot = Skill()
    >>> bot.reply(None)
    [(1.0, "What's your name? You just said None')]
    """

    def __init__(self, *args, **kwargs):
        """ Load the v3.dialog.yaml file to initialize the dialog state machine (dialog engine) """
        self.level = 0
        super().__init__(*args, **kwargs)

    def reply(self, statement, context=None):
        """ Suggest responses to a user statement string with [(score, reply_string)..]"""

        responses = []
        if not self.level:
            responses.append(f"What's your name? You just said {statement}")
        elif self.level > 0:
            responses.append(f"bye bye {statement}")
        self.level += 1
        normalize_replies(responses)
        return responses
