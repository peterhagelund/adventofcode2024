DELTAS = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
]


def find_start(track: list[str]) -> tuple[int, int]:
    for y in range(len(track)):
        for x in range(len(track[y])):
            if track[y][x] == 'S':
                return (y, x)
    return 0, 0


def calculate_distances(track: list[str], y: int, x: int) -> list[list[int]]:
    height = len(track)
    width = len(track[0])
    distances = [[-1] * width for _ in range(height)]
    distances[y][x] = 0
    while track[y][x] != 'E':
        for delta in DELTAS:
            _y, _x = y + delta[0], x + delta[1]
            if _y < 0 or _y >= height or _x < 0 or _x >= width:
                continue
            if track[_y][_x] == '#':
                continue
            if distances[_y][_x] != -1:
                continue
            distances[_y][_x] = distances[y][x] + 1
            y, x = _y, _x
    return distances


def main():
    track: list[str] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            track.append(line.strip())
    y, x = find_start(track)
    assert (y, x) != (0, 0)
    distances = calculate_distances(track, y, x)
    height = len(track)
    width = len(track[0])
    answer = 0
    for y in range(height):
        for x in range(width):
            if track[y][x] == '#':
                continue
            for distance in range(2, 21):
                for dy in range(distance + 1):
                    dx = distance - dy
                    deltas = [
                        (dy, dx),
                        (dy, -dx),
                        (-dy, dx),
                        (-dy, -dx),
                    ]
                    cheats = set([(y + delta[0], x + delta[1]) for delta in deltas])
                    for _y, _x in cheats:
                        if _y < 0 or _y >= height or _x < 0 or _x >= width:
                            continue
                        if track[_y][_x] == '#':
                            continue
                        if distances[y][x] - distances[_y][_x] >= 100 + distance:
                            answer += 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
