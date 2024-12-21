from collections import deque

DELTAS = [
    (-1, 0),
    (0, -1),
    (1, 0),
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


def calculate_price(plots: set[tuple[int, int]]) -> int:
    area = len(plots)
    sides = 0
    keys = [
        lambda p: (p[0], p[1]),
        lambda p: (p[1], p[0]),
        lambda p: (-p[0], p[1]),
        lambda p: (-p[1], p[0]),
    ]
    for orientation in range(4):
        _plots = sorted(plots, key=keys[orientation])
        runs: list[list[tuple[int, int]]] = []
        run: list[tuple[int, int]] = None
        if orientation == 0 or orientation == 2:
            # Vertical:
            _y, _x = -1, -1
            for y, x in _plots:
                if y != _y or x != _x + 1:
                    if run is not None:
                        runs.append(run)
                        run = None
                    _y = y
                    _x = x
                if run is None:
                    run = []
                run.append((y, x))
                _x = x
            if run is not None:
                runs.append(run)
        else:
            # Horizontal:
            _y, _x = -1, -1
            for y, x in _plots:
                if x != _x or y != _y + 1:
                    if run is not None:
                        runs.append(run)
                        run = None
                    _y = y
                    _x = x
                if run is None:
                    run = []
                run.append((y, x))
                _y = y
            if run is not None:
                runs.append(run)
        for run in runs:
            side = False
            for y, x in run:
                if (y + DELTAS[orientation][0], x + DELTAS[orientation][1]) not in plots:
                    if not side:
                        sides += 1
                        side = True
                else:
                    side = False
    return area * sides


def main():
    garden: list[str] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            garden.append(line.strip())
    seen: set[tuple[int, int]] = set()
    answer = 0
    count = 0
    for y in range(len(garden)):
        for x in range(len(garden[y])):
            pos = (y, x)
            if pos in seen:
                continue
            plots = find_region(garden, pos)
            seen.update(plots)
            answer += calculate_price(plots)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
