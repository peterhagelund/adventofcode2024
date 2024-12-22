from io import StringIO

WALL = ord('#')
BOX = ord('O')
ROBOT = ord('@')
SPACE = ord('.')


def print_warehouse(warehouse: list[bytearray]):
    for b in warehouse:
        print(b.decode())


def find_robot_pos(warehouse: list[bytearray]) -> tuple[int, int]:
    for y in range(len(warehouse)):
        for x in range(len(warehouse[y])):
            if warehouse[y][x] == ROBOT:
                return (y, x)
    return (-1, -1)


def move_box(warehouse: list[bytearray], y: int, x: int, dy: int, dx: int):
    _y, _x = y + dy, x + dx
    if warehouse[_y][_x] == WALL:
        return
    if warehouse[_y][_x] == BOX:
        move_box(warehouse, _y, _x, dy, dx)
    if warehouse[_y][_x] == SPACE:
        warehouse[_y][_x] = BOX
        warehouse[y][x] = SPACE


def main():
    warehouse: list[bytearray] = []
    builder = StringIO()
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            if line[0] == '#':
                warehouse.append(bytearray(line.strip(), 'utf-8'))
            else:
                builder.write(line.strip())
    movements = builder.getvalue()
    y, x = find_robot_pos(warehouse)
    for movement in movements:
        match movement:
            case '^':
                dy, dx = -1, 0
            case 'v':
                dy, dx = 1, 0
                _y, _x = y - +1, x
            case '<':
                dy, dx = 0, -1
            case '>':
                dy, dx = 0, 1
        _y, _x = y + dy, x + dx
        if warehouse[_y][_x] == WALL:
            continue
        if warehouse[_y][_x] == BOX:
            move_box(warehouse, _y, _x, dy, dx)
        if warehouse[_y][_x] == SPACE:
            warehouse[_y][_x] = ROBOT
            warehouse[y][x] = SPACE
            y, x = _y, _x
    answer = 0
    for y in range(len(warehouse)):
        for x in range(len(warehouse[y])):
            if warehouse[y][x] != BOX:
                continue
            answer += y * 100 + x
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
