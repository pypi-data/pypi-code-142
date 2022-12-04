""""Модуль с тестами для функции to_sum_of_squartes() """

from .to_sum_of_squares import to_sum_of_squares


class TestClass:
    def test_one(self):
        assert to_sum_of_squares(0, 0) == []

    def test_two(self):
        assert to_sum_of_squares(0, 5) == [0]

    def test_free(self):
        assert to_sum_of_squares(20, 4) == [1, 1, 9, 9]

    def test_four(self):
        assert to_sum_of_squares(27, 3) == [1, 1, 25]

    def test_five(self):
        assert to_sum_of_squares(38, 2) is None


# pytest(TestClass())
