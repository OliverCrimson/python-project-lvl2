import argparse

from gendiff.convertation import convert
from gendiff.flat_differ import generate_diff



parser = argparse.ArgumentParser(
    description="Compares two configuration files and shows a difference"
)
parser.add_argument("-f", "--format", help='set format of output')
parser.add_argument("a", help='first file')
parser.add_argument("b", help='second file')

args = parser.parse_args()

x = convert(args.a)
y = convert(args.b)

result = generate_diff(x, y)


def main():
    print(result)


if __name__ == "__main__":
    main()
