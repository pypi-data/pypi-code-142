from py_cover_letters.db.models import CoverLetter


def test_attributes():
    cover_letter = CoverLetter().dict()
    expected_fields = {'cover_template', 'date_generated', 'date_sent_via_email', 'delete', 'description', 'greeting',
                       'id', 'to_email'}
    # print(CoverLetter.__fields__.keys())
    assert set(cover_letter.keys()) == expected_fields
