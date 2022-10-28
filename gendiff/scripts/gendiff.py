# !/usr/bin/env python3
from gendiff.diff import generate_diff
from gendiff.cli import parsing


def main():
    arguments = parsing()
    result = generate_diff(
        arguments.first_file,
        arguments.second_file,
        arguments.format
    )
    print(result)


if __name__ == '__main__':
    main()
