import re

PV = r'p=(\d+),(\d+) v=(-?\d+),(-?\d+)'
WIDTH = 101
HEIGHT = 103


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

    def get_quadrant(self) -> int:
        hm = WIDTH // 2
        vm = HEIGHT // 2
        if self.x == hm or self.y == vm:
            return -1
        if self.x < hm:
            if self.y < vm:
                return 0
            else:
                return 2
        else:
            if self.y < vm:
                return 1
            else:
                return 3

    def __repr__(self):
        return f'Robot[x={self.x}, y={self.y}, dx={self.dx}, dy={self.dy}]'


def main():
    robots: list[Robot] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            g = re.match(PV, line).groups()
            robots.append(Robot(int(g[0]), int(g[1]), int(g[2]), int(g[3])))
    for _ in range(100):
        for robot in robots:
            robot.move()
    counts = [0, 0, 0, 0]
    for robot in robots:
        quadrant = robot.get_quadrant()
        if quadrant == -1:
            continue
        counts[quadrant] += 1
    answer = 1
    for count in counts:
        answer *= count
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
