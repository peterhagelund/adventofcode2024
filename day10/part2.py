from collections import deque

DELTAS = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
]


def find_trail_heads(map: list[list[int]]) -> list[tuple[int, int]]:
    trail_heads: list[tuple[int, int]] = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 0:
                trail_heads.append((y, x))
    return trail_heads


def get_path_count(map: list[list[int]], y: int, x: int) -> int:
    count = 0
    height = len(map)
    width = len(map[0])
    queue: deque[tuple[int, int]] = deque([(y, x)])
    while queue:
        y, x = queue.pop()
        elevation = map[y][x]
        for dy, dx in DELTAS:
            _y = y + dy
            _x = x + dx
            if _y < 0 or _y == height or _x < 0 or _x == width:
                continue
            if map[_y][_x] - elevation != 1:
                continue
            if map[_y][_x] == 9:
                count += 1
                continue
            queue.append((_y, _x))
    return count


def main():
    map: list[list[int]] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            map.append([int(c) for c in line.strip()])
    trail_heads = find_trail_heads(map)
    answer = 0
    for y, x in trail_heads:
        answer += get_path_count(map, y, x)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
