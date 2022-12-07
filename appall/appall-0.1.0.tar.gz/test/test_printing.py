from unittest import TestCase

from appall import AppallingLogger


class TestPrinting(TestCase):
    def test_one_line_printing(self):
        i = 0

        def print_(message):
            nonlocal i

            i += 1
            self.assertEqual(message, "foo bar baz ")

        logger = AppallingLogger(print_)
        logger.log('foo')
        logger.loop()
        logger.log('bar')
        logger.log('baz')

        logger.print(column_width = 4)

        self.assertEqual(i, 1, 'custom print has never been executed')

    def test_two_line_printing(self):
        i = 0

        def print_(message):
            nonlocal i

            if i == 0:
                self.assertEqual(message, "foo bar baz ")
            else:
                self.assertEqual(message, "qux quuxquuz")

            i += 1

        logger = AppallingLogger(print_)
        logger.log('foo')
        logger.log('qux')
        logger.loop()

        logger.log('bar')
        logger.log('quux')

        logger.log('baz')
        logger.log('quuz')

        logger.print(column_width = 4)

        self.assertEqual(i, 2, 'custom print has never been executed')

    def test_single_loop_call(self):
        logger = AppallingLogger(lambda x: x)
        logger.log('foo')
        logger.log('qux')
        logger.loop()

        logger.log('bar')
        logger.log('quux')

        self.assertRaises(ValueError, lambda: logger.loop())
