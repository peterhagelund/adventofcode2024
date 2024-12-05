import re


def main():
    enabled = True
    pattern = r'do\(\)|don\'t\(\)|mul\([0-9]{1,3},[0-9]{1,3}\)'
    with open('puzzle_input.txt', 'rt') as f:
        answer = 0
        for line in f:
            instructions = re.findall(pattern, line)
            for instruction in instructions:
                match instruction:
                    case 'do()':
                        enabled = True
                    case 'don\'t()':
                        enabled = False
                    case _:
                        if enabled:
                            values = [int(v) for v in instruction[4:-1].split(',')]
                            answer += values[0] * values[1]
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
