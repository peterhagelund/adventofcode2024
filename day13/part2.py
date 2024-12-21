import re

BUTTON_A = r'^Button A: X\+(\d+), Y\+(\d+)$'
BUTTON_B = r'^Button B: X\+(\d+), Y\+(\d+)$'
PRIZE = r'^Prize: X=(\d+), Y=(\d+)$'
ADJUSTMENT = 10_000_000_000_000


def find_cheapest_way(a: tuple[int, int], b: tuple[int, int], p: tuple[int, int]) -> int:
    a1, b1, c1 = a[0], b[0], p[0]
    a2, b2, c2 = a[1], b[1], p[1]
    d = a1 * b2 - a2 * b1
    if d == 0:
        return 0
    dx = c1 * b2 - c2 * b1
    dy = a1 * c2 - a2 * c1
    _a = dx / d
    _b = dy / d
    if int(_a) == _a and int(_b) == _b:
        return int(_a * 3 + _b)
    return 0


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
                    p = (int(g[0]) + ADJUSTMENT, int(g[1]) + ADJUSTMENT)
                    answer += find_cheapest_way(a, b, p)
                case _:
                    counter = 0
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
