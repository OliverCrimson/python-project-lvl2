import argparse

parser = argparse.ArgumentParser(
    description="Compares two configuration files and shows a difference"
)
parser.add_argument("-f", "--format", help='set format of output')
parser.add_argument("a", help='first file')
parser.add_argument("b", help='second file')

args = parser.parse_args()