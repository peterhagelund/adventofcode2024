import heapq


def main():
    maze: list[str] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            maze.append(line.strip())
    y, x = len(maze) - 2, 1
    assert maze[y][x] == 'S'
    queue: list[tuple[int, int, int, int, int]] = []
    seen: set[tuple[int, int, int, int, int]] = set()
    queue.append((0, y, x, 0, 1))
    seen.add((y, x, 0, 1))
    answer = 0
    while queue:
        cost, y, x, dy, dx = heapq.heappop(queue)
        seen.add((y, x, dy, dx))
        if maze[y][x] == 'E':
            answer = cost
            break
        for _cost, _y, _x, _dy, _dx in [(cost + 1, y + dy, x + dx, dy, dx), (cost + 1000, y, x, dx, -dy), (cost + 1000, y, x, -dx, dy)]:
            if maze[_y][_x] == '#':
                continue
            if (_y, _x, _dy, _dx) in seen:
                continue
            heapq.heappush(queue, (_cost, _y, _x, _dy, _dx))
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
