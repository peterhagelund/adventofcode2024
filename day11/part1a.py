def count_stones(stone: int, blinks: int, blink: int) -> int:
    if blink == blinks:
        return 1
    if stone == 0:
        return count_stones(1, blinks, blink + 1)
    s = str(stone)
    if len(s) % 2 == 0:
        return count_stones(int(s[: len(s) // 2]), blinks, blink + 1) + count_stones(int(s[len(s) // 2 :]), blinks, blink + 1)
    return count_stones(stone * 2024, blinks, blink + 1)


def main():
    with open('puzzle_input.txt', 'rt') as f:
        stones = [int(s) for s in f.read().strip().split()]
    answer = 0
    for stone in stones:
        answer += count_stones(stone, 25, 0)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
