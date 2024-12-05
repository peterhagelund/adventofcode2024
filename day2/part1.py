def is_safe(levels: list[int]) -> bool:
    asc = sorted(levels)
    desc = sorted(levels, reverse=True)
    if levels != asc and levels != desc:
        return False
    for i in range(1, len(levels)):
        delta = abs(levels[i] - levels[i - 1])
        if delta < 1 or delta > 3:
            return False
    return True


def main():
    answer = 0
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            levels = [int(l) for l in line.strip().split()]
            if is_safe(levels):
                answer += 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
