def count_stones(stone: int, blinks: int, blink: int, count: int) -> int:
    if blink < blinks:
        if stone == 0:
            n1, n2 = 1, None
        else:
            s = str(stone)
            if len(s) % 2 == 0:
                n1 = int(s[: len(s) // 2])
                n2 = int(s[len(s) // 2 :])
            else:
                n1, n2 = stone * 2024, None
        if n2 is None:
            _count = count_stones(n1, blinks, blink + 1, count)
        else:
            _count = count_stones(n1, blinks, blink + 1, count)
            _count += count_stones(n2, blinks, blink + 1, 1)
    else:
        _count = count
    return _count


def main():
    with open('puzzle_input.txt', 'rt') as f:
        stones = [int(s) for s in f.read().strip().split()]
    answer = 0
    for stone in stones:
        answer += count_stones(stone, 25, 0, 1)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
