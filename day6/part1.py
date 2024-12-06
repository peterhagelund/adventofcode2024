GUARD = ord('^')
OBSTRUCTION = ord('#')
DELTAS = [
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),  # left
    (0, 1),  # right
]

DIRECTIONS = [3, 2, 0, 1]


def main():
    map: list[bytearray] = []
    pos: tuple[int, int] | None = None
    y = 0
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            row = bytearray(line.strip(), 'utf-8')
            x = row.find(GUARD)
            if x != -1:
                pos = (y, x)
            map.append(row)
            y += 1
    (y, x) = pos
    height, width = len(map), len(map[0])
    visited: set[tuple[int, int]] = {(y, x)}
    direction = 0
    while True:
        _y, _x = y + DELTAS[direction][0], x + DELTAS[direction][1]
        if _y < 0 or _y == height or _x < 0 or _x == width:
            break
        if map[_y][_x] == OBSTRUCTION:
            direction = DIRECTIONS[direction]
        else:
            y, x = _y, _x
            visited.add((y, x))
    print(f'answer = {len(visited)}')


if __name__ == '__main__':
    main()
