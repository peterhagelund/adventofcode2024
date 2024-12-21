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


def calculate_price(plots: set[tuple[int, int]]) -> int:
    area = len(plots)
    _plots = sorted(plots)
    print(_plots)
    layers: list[list[tuple[int, int]]] = []
    layer: list[tuple[int, int]] | None = None
    y = -1
    for pos in _plots:
        if pos[0] != y:
            if layer is not None:
                layers.append(layer)
                layer = None
            y = pos[0]
        if layer is None:
            layer = []
        layer.append(pos[1])
    if layer is not None:
        layers.append(layer)
    sides = 0
    start_x = -1
    end_x = -1
    for y in range(len(layers)):
        layer = layers[y]
        if y == 0:
            sides += 3
            start_x = layer[0]
            end_x = layer[-1]
        else:
            if layer[0] != start_x:
                sides += 2
                start_x = layer[0]
            if layer[-1] != end_x:
                sides += 2
                end_x = layer[-1]
    sides += 1
    print(f'area = {area}, sides = {sides}')
    return area * sides


def main():
    garden: list[str] = []
    with open('example_input.txt', 'rt') as f:
        for line in f:
            garden.append(line.strip())
    seen: set[tuple[int, int]] = set()
    answer = 0
    for y in range(len(garden)):
        for x in range(len(garden[y])):
            pos = (y, x)
            if pos in seen:
                continue
            print(f'plant = {garden[y][x]}:')
            plots = find_region(garden, pos)
            seen.update(plots)
            answer += calculate_price(plots)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
