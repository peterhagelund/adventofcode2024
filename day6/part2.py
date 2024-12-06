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


def walk_guard_route(map: list[str], y: int, x: int) -> bool:
    turns: set[tuple[int, int, Direction]] = set()
    loop = False
    height = len(map)
    width = len(map[0])
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
            turn = (y, x, direction)
            if turn in turns:
                loop = True
                break
            turns.add(turn)
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
    return loop


def main():
    map: list[str] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            map.append(line.strip())
    pos = find_guard_start(map)
    assert pos is not None
    (start_y, start_x) = pos
    answer = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] != '.':
                continue
            _map: list[str] = []
            for i in range(len(map)):
                row = map[i]
                if i != y:
                    _map.append(row)
                else:
                    _map.append(row[:x] + '#' + row[x + 1 :])
            loop = walk_guard_route(_map, start_y, start_x)
            if loop:
                answer += 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
