import heapq
from collections import deque
from sys import maxsize


def main():
    maze: list[str] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            maze.append(line.strip())
    y, x = len(maze) - 2, 1
    assert maze[y][x] == 'S'
    queue: list[tuple[int, int, int, int, int]] = []
    queue.append((0, y, x, 0, 1))
    costs: dict[tuple[int, int, int, int], int] = {}
    lowest_cost = maxsize
    end_states: set[tuple[int, int, int, int]] = set()
    backtrack: dict[tuple[int, int, int, int], set[tuple[int, int, int, int]]] = {}
    dummy: set[tuple[int, int, int, int]] = set()
    answer = 0
    while queue:
        cost, y, x, dy, dx = heapq.heappop(queue)
        if cost > costs.get((y, x, dy, dx), maxsize):
            continue
        if maze[y][x] == 'E':
            if cost > lowest_cost:
                break
            lowest_cost = cost
            end_states.add((y, x, dy, dx))
        for _cost, _y, _x, _dy, _dx in [(cost + 1, y + dy, x + dx, dy, dx), (cost + 1000, y, x, dx, -dy), (cost + 1000, y, x, -dx, dy)]:
            if maze[_y][_x] == '#':
                continue
            _lowest_cost = costs.get((_y, _x, _dy, _dx), maxsize)
            if _cost > _lowest_cost:
                continue
            if _cost < _lowest_cost:
                backtrack[(_y, _x, _dy, _dx)] = set()
                costs[(_y, _x, _dy, _dx)] = _cost
            backtrack[(_y, _x, _dy, _dx)].add((y, x, dy, dx))
            heapq.heappush(queue, (_cost, _y, _x, _dy, _dx))
    queue: deque[tuple[int, int, int, int]] = deque(end_states)
    seen: set[tuple[int, int, int, int]] = set(end_states)
    while queue:
        state = queue.popleft()
        for last in backtrack.get(state, dummy):
            if last in seen:
                continue
            seen.add(last)
            queue.append(last)
    answer = len({(y, x) for y, x, _, _ in seen})
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
