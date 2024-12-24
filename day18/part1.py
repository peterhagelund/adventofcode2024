import heapq

DIMENSION = 71
COUNT = 1024
SAFE = ord('.')
CORRUPTED = ord('#')
DELTAS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]


def main():
    mem_space = [bytearray([SAFE for _ in range(DIMENSION)]) for _ in range(DIMENSION)]
    count = 0
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            pos = [int(s) for s in line.split(',')]
            x, y = pos[0], pos[1]
            mem_space[y][x] = CORRUPTED
            count += 1
            if count == COUNT:
                break
    queue: list[tuple[int, int, int]] = []
    seen: set[tuple[int, int]] = set()
    queue.append((0, 0, 0))
    seen.add((0, 0))
    answer = 0
    while queue:
        steps, y, x = heapq.heappop(queue)
        if y == DIMENSION - 1 and x == DIMENSION - 1:
            answer = steps
            break
        for delta in DELTAS:
            _y, _x = y + delta[0], x + delta[1]
            if 0 <= _y < DIMENSION and 0 <= _x < DIMENSION:
                if mem_space[_y][_x] == CORRUPTED:
                    continue
                if (_y, _x) in seen:
                    continue
                heapq.heappush(queue, (steps + 1, _y, _x))
                seen.add((_y, _x))
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
