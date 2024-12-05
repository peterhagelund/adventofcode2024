def main():
    puzzle: list[str] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            puzzle.append(line.strip())
    answer = 0
    for y in range(1, len(puzzle) - 1):
        for x in range(1, len(puzzle[0]) - 1):
            if puzzle[y][x] != 'A':
                continue
            if (puzzle[y - 1][x - 1] == 'M' and puzzle[y + 1][x + 1] == 'S') or (puzzle[y - 1][x - 1] == 'S' and puzzle[y + 1][x + 1] == 'M'):
                if (puzzle[y + 1][x - 1] == 'M' and puzzle[y - 1][x + 1] == 'S') or (puzzle[y + 1][x - 1] == 'S' and puzzle[y - 1][x + 1] == 'M'):
                    answer += 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
