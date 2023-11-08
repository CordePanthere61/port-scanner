import sys

from models.scanner import Scanner
from models.target import Target


def main():
    args = sys.argv
    print(args)
    if len(args) < 2:
        sys.exit("Must give arguments")

    Scanner().scan(Target(sys.argv)).print_result()


if __name__ == '__main__':
    main()
