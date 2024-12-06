from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3


def find_guard_start(map: list[str]) -> tuple[int, int] | None:
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '^':
                return (y, x)
    return None


def main():
    map: list[str] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            map.append(line.strip())
    pos = find_guard_start(map)
    assert pos is not None
    (y, x) = pos
    height = len(map)
    width = len(map[0])
    visited: set[tuple[int, int]] = {(y, x)}
    direction = Direction.UP
    while True:
        match direction:
            case Direction.UP:
                _y, _x = y - 1, x
            case Direction.DOWN:
                _y, _x = y + 1, x
            case Direction.LEFT:
                _y, _x = y, x - 1
            case Direction.RIGHT:
                _y, _x = y, x + 1
        if _y < 0 or _y == height or _x < 0 or _x == width:
            break
        if map[_y][_x] == '#':
            match direction:
                case Direction.UP:
                    direction = Direction.RIGHT
                case Direction.DOWN:
                    direction = Direction.LEFT
                case Direction.LEFT:
                    direction = Direction.UP
                case Direction.RIGHT:
                    direction = Direction.DOWN
        else:
            y, x = _y, _x
            visited.add((y, x))
    print(f'answer = {len(visited)}')


if __name__ == '__main__':
    main()
