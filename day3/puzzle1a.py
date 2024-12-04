import re

print(f'sum = {sum([int(i[0]) * int(i[1]) for i in [i for il in [re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', l) for l in open('puzzle_input.txt', 'rt')] for i in il]])}')
