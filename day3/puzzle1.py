import re


def main():
    with open('puzzle_input.txt', 'rt') as f:
        sum = 0
        for line in f:
            instructions = re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', line)
            for instruction in instructions:
                values = [int(v) for v in instruction[4:-1].split(',')]
                sum += values[0] * values[1]
    print(f'sum = {sum}')


if __name__ == '__main__':
    main()
