import re


def main():
    with open('puzzle_input.txt', 'rt') as f:
        answer = 0
        for line in f:
            instructions = re.findall(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)', line)
            values = [(int(i[0]), int(i[1])) for i in instructions]
            answer += sum([v[0] * v[1] for v in values])
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
