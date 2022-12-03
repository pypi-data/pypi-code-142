import inspect
from pathlib import Path

from py_cover_letters import ConfigurationManager
from py_cover_letters.db.sqlite import CoverLetterManager
from py_cover_letters.enums import FilterType
from tests.factories import CoverLetterFactory


class TestCoverLetterManager:

    def test_create(self, testing_database_file):
        manager = CoverLetterManager(testing_database_file)

        cover_letter = CoverLetterFactory.create(new=True)

        assert cover_letter.id is None

        db_cover_letter = manager.create(cover_letter)

        assert db_cover_letter.id is not None
        assert cover_letter.id is not None

    def test_filter_deleted(self, cover_letter_manager):
        deleted = cover_letter_manager.filter(FilterType.COVER_LETTER_NOT_DELETED)
        all_cover_letters = cover_letter_manager.list()
        assert len(deleted) == 11
        assert len(all_cover_letters) == 13

    def test_filter_not_created(self, cover_letter_manager):
        not_created = cover_letter_manager.filter(FilterType.COVER_LETTER_NOT_CREATED)
        all_cover_letters = cover_letter_manager.list()
        assert len(not_created) == 8
        assert len(all_cover_letters) == 13


def test_inspect():
    sf = Path(inspect.getsourcefile(ConfigurationManager)).parent / 'templates'
    home_folder = Path.home()
    assert str(sf) == f'{home_folder}/PycharmProjects/py_cover_letters/py_cover_letters/templates'
