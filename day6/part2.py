GUARD = ord('^')
DOT = ord('.')
OBSTRUCTION = ord('#')
DELTAS = [
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),  # left
    (0, 1),  # right
]
DIRECTIONS = [3, 2, 0, 1]


def walk_guard_route(map: list[bytearray], y: int, x: int, visits=False) -> tuple[set[tuple[int, int]], bool]:
    visited: set[tuple[int, int]] | None = None
    if visits:
        visited = set()
    loop = False
    turns: list[tuple[int, int, int]] | None = None
    if not visits:
        turns = set()
    height = len(map)
    width = len(map[0])
    direction = 0
    while True:
        _y, _x = y + DELTAS[direction][0], x + DELTAS[direction][1]
        if _y < 0 or _y == height or _x < 0 or _x == width:
            break
        if map[_y][_x] == OBSTRUCTION:
            if not visits:
                turn = (y, x, direction)
                if turn in turns:
                    loop = True
                    break
                turns.add(turn)
            direction = DIRECTIONS[direction]
        else:
            y, x = _y, _x
            if visits:
                visited.add((y, x))
    return (visited, loop)


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
    assert pos is not None
    (start_y, start_x) = pos
    visited, _ = walk_guard_route(map, start_y, start_x, visits=True)
    answer = 0
    for y, x in visited:
        if y == start_y and x == start_x:
            continue
        map[y][x] = OBSTRUCTION
        _, loop = walk_guard_route(map, start_y, start_x)
        map[y][x] = DOT
        if loop:
            answer += 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
