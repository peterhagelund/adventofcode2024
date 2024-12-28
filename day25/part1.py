def main():
    locks: list[list[int]] = []
    keys: list[list[int]] = []
    rows: list[str] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue
            rows.append(line)
            if len(rows) == 7:
                lock = rows[0] == '#####'
                if not lock:
                    rows.reverse()
                heights = [0] * 5
                for y in range(1, 7):
                    for x in range(5):
                        if rows[y][x] == '#':
                            heights[x] += 1
                if lock:
                    locks.append(heights)
                else:
                    keys.append(heights)
                rows.clear()
    answer = 0
    for key in keys:
        for lock in locks:
            overlaps = False
            for i in range(5):
                if key[i] + lock[i] > 5:
                    overlaps = True
                    break
            if not overlaps:
                answer += 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
