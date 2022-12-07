
def program(a1, a2):
    print(a1, a2)


def main():
    import sys
    arg1, arg2 = sys.argv[1], sys.argv[2]
    program(arg1, arg2)

if __name__ == "__main__":
    main()