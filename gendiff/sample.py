from gendiff.convertation import convert
from gendiff.flat_differ import generate_diff
import pprint
import 
first_file = convert('sample_one.json')
second_file = convert('sample_two.json')
x = generate_diff(first_file, second_file)

# pprint.pp(first_file)
# pprint.pp(second_file)

for i in first_file.values():
    print(i)