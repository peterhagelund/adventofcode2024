POS = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # Horizontal, left-to-right
    [(0, 0), (0, -1), (0, -2), (0, -3)],  # Horizontal, right-to-left
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # Vertical, top-to-bottom
    [(0, 0), (-1, 0), (-2, 0), (-3, 0)],  # Vertical, bottom-to-top
    [(0, 0), (1, 1), (2, 2), (3, 3)],  # Diagonal, top-left-to-bottom-right
    [(0, 0), (1, -1), (2, -2), (3, -3)],  # Diagonal, top-right-to-bottom-left
    [(0, 0), (-1, -1), (-2, -2), (-3, -3)],  # Diagonal, bottom-right-to-top-left
    [(0, 0), (-1, 1), (-2, 2), (-3, 3)],  # Diagonal, bottom-left-to-top-right
]

XMAS = 'XMAS'


def is_xmas(puzzle: list[str], y: int, x: int, pos: list[tuple[int, int]]) -> bool:
    for i in range(4):
        _y = y + pos[i][0]
        _x = x + pos[i][1]
        if _y < 0 or _y >= len(puzzle) or _x < 0 or _x >= len(puzzle[0]):
            return False
        if puzzle[_y][_x] != XMAS[i]:
            return False
    return True


def main():
    puzzle: list[str] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            puzzle.append(line.strip())
    answer = 0
    for y in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            for pos in POS:
                if is_xmas(puzzle, y, x, pos):
                    answer += 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
