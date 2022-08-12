import argparse

from gendiff.flat_differ import generate_diff, json_to_python

import pathlib

parser = argparse.ArgumentParser(
    description="Compares two configuration files and shows a difference"
)
parser.add_argument("-f", "--format", help='set format of output')
parser.add_argument("a", help='first file')
parser.add_argument("b", help='second file')

args = parser.parse_args()

x = json_to_python(args.a)
y = json_to_python(args.b)

result = generate_diff(x, y)


def main():
    print(result)


if __name__ == "__main__":
    main()
