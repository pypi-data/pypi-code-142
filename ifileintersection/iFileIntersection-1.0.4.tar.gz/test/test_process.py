import unittest
from contextlib import ExitStack

from intersection.main import find_intersection


class TestIntersection(unittest.TestCase):

    def test_find_intersection(self):
        find_intersection("data/file_1.txt", "data/file_2.txt", "data/output.txt", chunk_size=1)
        with ExitStack() as stack:
            output_file = stack.enter_context(open("data/output.txt", 'r'))
            actual = {int(val) for val in output_file.readlines()}

            file_1 = stack.enter_context(open("data/file_1.txt", 'r'))
            file_2 = stack.enter_context(open("data/file_2.txt", 'r'))
            expected = {int(val) for val in file_1} & {int(val) for val in file_2}
            self.assertSetEqual(expected, actual)

    def test_find_intersection_duplicate_data(self):
        find_intersection("data/duplicate_data_file_1.txt", "data/duplicate_data_file_2.txt", "data/output.txt",
                          chunk_size=1)
        with ExitStack() as stack:
            output_file = stack.enter_context(open("data/output.txt", 'r'))
            actual = {int(val) for val in output_file.readlines()}

            file_1 = stack.enter_context(open("data/duplicate_data_file_1.txt", 'r'))
            file_2 = stack.enter_context(open("data/duplicate_data_file_2.txt", 'r'))
            expected = {int(val) for val in file_1} & {int(val) for val in file_2}
            self.assertSetEqual(expected, actual)

    def test_find_intersection_arg_not_specified(self):
        with self.assertRaises(ValueError):
            find_intersection(None, "data/file_2.txt", "data/output.txt")
        with self.assertRaises(ValueError):
            find_intersection("data/file_1.txt", None, "data/output.txt")
        with self.assertRaises(ValueError):
            find_intersection("data/file_1.txt", "data/file_2.txt", None)

    def test_find_intersection_input_file_not_present(self):
        with self.assertRaises(FileNotFoundError):
            find_intersection("Unknown/path", "data/file_2.txt", "data/output.txt")
        with self.assertRaises(FileNotFoundError):
            find_intersection("data/file_1.txt", "Unknown/path", "data/output.txt")
