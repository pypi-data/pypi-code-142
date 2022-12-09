import argparse
import random
import string
import math


def main():
    def get_args():
        parser = argparse.ArgumentParser(description="Generate a random secret")
        parser.add_argument(
            "length", type=int, help="How many characters should the secret be?"
        )
        parser.add_argument(
            "-n",
            "--numbers",
            default=10,
            type=int,
            help="numbers percentage of total length defaults to 10",
        )
        parser.add_argument(
            "-s",
            "--specials",
            type=int,
            default=10,
            help="special character percentage of total length defaults to 10",
        )
        return parser.parse_args()

    def randomizer(length, chars):
        foo = []
        for _ in range(0, length):
            foo.append(chars[random.randint(-1, len(chars) - 1)])
        return foo

    args = get_args()
    letters = string.ascii_letters
    nums = string.digits
    specs = "!@#$%^*-_+="

    nums_length = math.ceil((args.length / 100) * args.numbers)
    specs_length = math.ceil((args.length / 100) * args.specials)
    letters_length = args.length - nums_length - specs_length

    letters = randomizer(letters_length, letters)
    nums = randomizer(nums_length, nums)
    specs = randomizer(specs_length, specs)
    chars = letters + nums + specs
    random.shuffle(chars)
    secret = "".join(chars)
    print(secret)


if __name__ == "__main__":
    main()
