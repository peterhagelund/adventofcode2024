import re

BUTTON_A = r'^Button A: X\+(\d+), Y\+(\d+)$'
BUTTON_B = r'^Button B: X\+(\d+), Y\+(\d+)$'
PRIZE = r'^Prize: X=(\d+), Y=(\d+)$'


def find_cheapest_way(a: tuple[int, int], b: tuple[int, int], p: tuple[int, int]) -> int:
    x, y = p
    options: list[tuple[int, int]] = []
    for a_presses in range(101):
        for b_presses in range(101):
            if a[0] * a_presses + b[0] * b_presses == x and a[1] * a_presses + b[1] * b_presses == y:
                options.append((a_presses, b_presses))
    if len(options) == 0:
        return 0
    cost = sorted([o[0] * 3 + o[1] for o in options])
    return cost[0]


def main():
    answer = 0
    with open('puzzle_input.txt', 'rt') as f:
        counter = 0
        for line in f:
            counter += 1
            match counter:
                case 1:
                    g = re.match(BUTTON_A, line).groups()
                    a = (int(g[0]), int(g[1]))
                case 2:
                    g = re.match(BUTTON_B, line).groups()
                    b = (int(g[0]), int(g[1]))
                case 3:
                    g = re.match(PRIZE, line).groups()
                    p = (int(g[0]), int(g[1]))
                    answer += find_cheapest_way(a, b, p)
                case _:
                    counter = 0
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
