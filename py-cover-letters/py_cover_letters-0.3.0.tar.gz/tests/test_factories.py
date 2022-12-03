from tests.factories import CoverLetterFactory


class TestCoverLetterFactory:

    def test_create(self):
        cover_letter = CoverLetterFactory.create()
        cover_letter_dict = cover_letter.dict()
        expected_fields = {'company_name', 'cover_template', 'date_generated', 'date_sent_via_email', 'description',
                           'greeting', 'id', 'position_name', 'delete', 'to_email'}
        assert set(cover_letter_dict.keys()) == expected_fields

    def test_new_trait(self):
        cover_letter = CoverLetterFactory.create(new=True)
        assert cover_letter.id is None
        assert cover_letter.date_generated is None
