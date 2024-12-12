def count_stones(stone: int, blinks: int, blink: int, count: int, cache: dict[tuple[int, int], int]) -> int:
    key = (blink, stone)
    if key in cache:
        return cache[key]
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
            _count = count_stones(n1, blinks, blink + 1, count, cache)
        else:
            _count = count_stones(n1, blinks, blink + 1, count, cache)
            _count += count_stones(n2, blinks, blink + 1, 1, cache)
    else:
        _count = count
    cache[key] = _count
    return _count


def main():
    with open('puzzle_input.txt', 'rt') as f:
        stones = [int(s) for s in f.read().strip().split()]
    cache: dict[tuple[int, int], int] = {}
    answer = 0
    for stone in stones:
        answer += count_stones(stone, 75, 0, 1, cache)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
