from pathlib import Path

from factory import Factory
from factory import LazyAttribute, Trait
from factory import lazy_attribute
from faker import Factory as FakerFactory

from py_cover_letters import ConfigurationManager
from py_cover_letters.db.models import CoverLetter

faker = FakerFactory.create()

TIME_ZONE = None  # 'America/Panama'


class CoverLetterFactory(Factory):
    class Meta:
        model = CoverLetter

    class Params:
        new = Trait(
            id=None,
            date_generated=None
        )
        no_email = Trait(
            to_email=None
        )

    id = LazyAttribute(lambda x: faker.random_int(min=100))
    company_name = LazyAttribute(lambda x: faker.company())
    position_name = LazyAttribute(lambda x: faker.job())
    greeting = 'Dear Hiring manager'
    to_email = LazyAttribute(lambda x: faker.email())
    cover_template = 'Cover Letter Template.docx'
    date_generated = LazyAttribute(lambda x: faker.date_time_between(start_date="-1m",
                                                                     end_date="now", tzinfo=None))
    description = 'New position'
    delete = False

    @lazy_attribute
    def date_sent_via_email(self):
        return self.date_generated


class TestingConfigurationManager(ConfigurationManager):
    def __init__(self, config_file: Path):
        super(TestingConfigurationManager, self).__init__(config_file.parent,
                                                          config_filename=config_file.name)
