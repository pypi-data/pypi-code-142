from new_diap import new_diap
from to_sum_of_squares import to_sum_of_squares
import argparse as args


def main():
        parser = args.ArgumentParser()
        parser.add_argument("--diap", type=str, help="Введите диапазон", nargs="+")
        arg = parser.parse_args()
        print(arg.diap)
        if len(arg.diap) == 2:
            diap = f"{arg.diap[0]} {arg.diap[1]}"
        else:
            diap = f"{arg.diap[0]}"
        start_stop = new_diap(diap)
        if isinstance(start_stop, tuple):
            for number in range(start_stop[0], start_stop[1] + 1):
                if number == 1:
                    if number == 0:
                        print("попробуйте не вводить 0")
                    continue
                for k in range(1, 5):
                    decompose = to_sum_of_squares(number, k)
                    if decompose:
                        print("Согласно теореме Лагранжа число", number,
                              "состоит из следующих чисел, являющихся квадратами:", decompose)
                        break


if __name__ == '__main__':
    main()
