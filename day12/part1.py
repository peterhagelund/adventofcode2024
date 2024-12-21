from collections import deque

DELTAS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]


def find_region(garden: list[str], pos: tuple[int, int]) -> set[tuple[int, int]]:
    queue = deque([pos])
    height = len(garden)
    width = len(garden[0])
    y, x = pos
    plant = garden[y][x]
    plots: set[tuple[int, int]] = set([pos])
    while queue:
        y, x = queue.pop()
        for dy, dx in DELTAS:
            _y = y + dy
            _x = x + dx
            if _y < 0 or _y == height or _x < 0 or _x == width:
                continue
            if garden[_y][_x] != plant:
                continue
            pos = (_y, _x)
            if pos in plots:
                continue
            plots.add(pos)
            queue.append(pos)
    return plots


def calculate_price(garden: list[str], plots: set[tuple[int, int]]) -> int:
    height = len(garden)
    width = len(garden[0])
    area = len(plots)
    perimeter = 0
    for pos in plots:
        y, x = pos
        plant = garden[y][x]
        for dy, dx in DELTAS:
            _y = y + dy
            _x = x + dx
            if _y < 0 or _y == height or _x < 0 or _x == width:
                perimeter += 1
                continue
            if garden[_y][_x] != plant:
                perimeter += 1
    return area * perimeter


def main():
    garden: list[str] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            garden.append(line.strip())
    seen: set[tuple[int, int]] = set()
    answer = 0
    for y in range(len(garden)):
        for x in range(len(garden[y])):
            pos = (y, x)
            if pos in seen:
                continue
            plots = find_region(garden, pos)
            seen.update(plots)
            answer += calculate_price(garden, plots)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
