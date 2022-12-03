import argparse
import pytest
from choice_sort_pack import input_check, choice_sort


parser = argparse.ArgumentParser()

parser.add_argument('list', nargs='?', default=False)
parser.add_argument('-t', dest='test_choice', action='store_true')
parser.add_argument('-d', dest='doctest_choice', action='store_true')
args = parser.parse_args()


def main():
    """
    Обработка выбранного пользователем действия.
    Обрабатывывает введённое пользователем через командную строку действие,
    проверяя его на идентичность с True.
    """
    match True:
        case args.test_choice:
            print(pytest.main(['-v']))
        case args.doctest_choice:
            import doctest
            doctest.testfile('choice_sort.py')
        case _:
            try:
                sort_list = input_check.input_raw_list(args.list)
            except AttributeError:
                print(
                        "Help menu:",
                        "python __main__.py 'massive's elements'",
                        "python __main__.py -t",
                        "python __main__.py -d",
                        sep='\n'
                        )
            else:
                if sort_list is not None:
                    print(
                        ' '.join(map(str, choice_sort.choice_sort(sort_list)))
                        )


if __name__ == '__main__':
    main()
