import re

PV = r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)'
WIDTH = 101
HEIGHT = 103

PATTERNS: list[list[tuple[int, int, bool]]] = [
    [(-1, -2, False), (-1, -1, False), (-1, 0, False), (-1, 1, False), (-1, 2, False)],
    [(0, -2, False), (0, -1, False), (0, 0, True), (0, 1, False), (0, 2, False)],
    [(1, -2, False), (1, -1, True), (1, 0, True), (1, 1, True), (1, 2, False)],
    [(2, -2, True), (2, -1, True), (2, 0, True), (2, 1, True), (2, 2, True)],
]


class Robot:
    def __init__(self, x: int, y: int, dx: int, dy: int):
        super().__init__()
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        x = self.x + self.dx
        if x < 0:
            x += WIDTH
        if x >= WIDTH:
            x -= WIDTH
        y = self.y + self.dy
        if y < 0:
            y += HEIGHT
        if y >= HEIGHT:
            y -= HEIGHT
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Robot[x={self.x}, y={self.y}, dx={self.dx}, dy={self.dy}]'


def print_tiles(locations: set[tuple[int, int]]):
    tiles = [bytearray(WIDTH) for _ in range(HEIGHT)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (y, x) in locations:
                tiles[y][x] = ord('*')
            else:
                tiles[y][x] = ord('.')
    for line in tiles:
        print(line.decode())


def main():
    robots: list[Robot] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            g = re.match(PV, line).groups()
            robots.append(Robot(int(g[0]), int(g[1]), int(g[2]), int(g[3])))
    answer = 0
    seconds = 0
    while answer == 0:
        locations: set[tuple[int, int]] = set()
        for robot in robots:
            robot.move()
            locations.add((robot.y, robot.x))
        seconds += 1
        if seconds < 6771:
            continue
        for y, x in locations:
            correct = 0
            for pattern in PATTERNS:
                for p in pattern:
                    l = (y + p[0], x + p[1])
                    if p[2] is True:
                        if l in locations:
                            correct += 1
                    else:
                        if l not in locations:
                            correct += 1
            if correct == 20:
                print('found it!')
                answer = seconds
                print_tiles(locations)
                break
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
