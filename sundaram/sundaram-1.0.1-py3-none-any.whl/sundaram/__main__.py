import argparse
import pytest
from sundaram import calculate_sundaram

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--test", dest="test_mod", action="store_true")
parser.add_argument("-d", "--doctest", dest="doctest_mod", action="store_true")
parser.add_argument("value", nargs="?", default=False)

args = parser.parse_args()
help_text = """
Алгоритм для расчёта решета Сундарама

Использование:
    sundaram [верхняя граница]
    sundaram -t [--test]
    sundaram -d [--doctest]

"""


def main():
    """
    Запуск sundarama как скрипта
    
    startup function for running a calc_happy as a script
    """
    if args.test_mod:
        retcode = pytest.main(["-v"])
        print(retcode)
        exit()
    if args.doctest_mod:
        import doctest
        doctest.testfile("test_sundaram.py")
        exit()
    if args.value is False:
        print(help_text)
    try:
        upper_limit = int(args.value)
        if upper_limit <= 1:
            print("Значение должно быть > 1")
            exit()
    except IndexError:
        print("Вы должны передать число")
        print(help_text)
        exit()
    except ValueError:
        print("Значение должно быть числом")
        exit()

    print(f"Расчет решета Сундарама в рамках [2,...,{upper_limit}]")

    print(calculate_sundaram(int(upper_limit)))

    print("Готово!")


if __name__ == "__main__":
    main()
