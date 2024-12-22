from io import StringIO

WALL = ord('#')
BOX_LEFT = ord('[')
BOX_RIGHT = ord(']')
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


def move_box_horizontally(warehouse: list[bytearray], y: int, x: int, dx: int):
    _x = x + dx * 2
    if warehouse[y][_x] == WALL:
        return
    if warehouse[y][_x] in [BOX_LEFT, BOX_RIGHT]:
        move_box_horizontally(warehouse, y, _x, dx)
    if warehouse[y][_x] == SPACE:
        warehouse[y][_x] = warehouse[y][x + dx]
        warehouse[y][x + dx] = warehouse[y][x]
        warehouse[y][x] = SPACE


def can_move_box_vertically(warehouse: list[bytearray], y: int, x: int, dy: int) -> bool:
    _y = y + dy
    if warehouse[y][x] == BOX_LEFT:
        left_x, right_x = x, x + 1
    else:
        left_x, right_x = x - 1, x
    if warehouse[_y][left_x] == WALL or warehouse[_y][right_x] == WALL:
        return False
    if warehouse[_y][left_x] == SPACE and warehouse[_y][right_x] == SPACE:
        return True
    if warehouse[_y][left_x] in [BOX_LEFT, BOX_RIGHT]:
        if not can_move_box_vertically(warehouse, _y, left_x, dy):
            return False
    if warehouse[_y][right_x] in [BOX_LEFT, BOX_RIGHT]:
        if not can_move_box_vertically(warehouse, _y, right_x, dy):
            return False
    return True


def move_box_vertically(warehouse: list[bytearray], y: int, x: int, dy: int):
    if not can_move_box_vertically(warehouse, y, x, dy):
        return
    _y = y + dy
    if warehouse[y][x] == BOX_LEFT:
        left_x, right_x = x, x + 1
    else:
        left_x, right_x = x - 1, x
    if warehouse[_y][left_x] in [BOX_LEFT, BOX_RIGHT]:
        move_box_vertically(warehouse, _y, left_x, dy)
    if warehouse[_y][right_x] in [BOX_LEFT, BOX_RIGHT]:
        move_box_vertically(warehouse, _y, right_x, dy)
    if warehouse[_y][left_x] == SPACE and warehouse[_y][right_x] == SPACE:
        warehouse[_y][left_x] = BOX_LEFT
        warehouse[_y][right_x] = BOX_RIGHT
        warehouse[y][left_x] = SPACE
        warehouse[y][right_x] = SPACE


def main():
    warehouse: list[bytearray] = []
    builder = StringIO()
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            if line[0] == '#':
                line = line.replace('#', '##')
                line = line.replace('.', '..')
                line = line.replace('O', '[]')
                line = line.replace('@', '@.')
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
        if warehouse[_y][_x] in [BOX_LEFT, BOX_RIGHT]:
            if dy == 0:
                move_box_horizontally(warehouse, _y, _x, dx)
            else:
                move_box_vertically(warehouse, _y, _x, dy)
        if warehouse[_y][_x] == SPACE:
            warehouse[_y][_x] = ROBOT
            warehouse[y][x] = SPACE
            y, x = _y, _x
    answer = 0
    for y in range(len(warehouse)):
        for x in range(len(warehouse[y])):
            if warehouse[y][x] != BOX_LEFT:
                continue
            answer += y * 100 + x
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
