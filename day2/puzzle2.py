def main():
    safe = 0
    with open("puzzle_input.txt", "rt") as f:
        for line in f:
            levels = [int(l) for l in line.strip().split()]
            if could_be_safe(levels):
                safe += 1
    print(f"safe = {safe}")


def could_be_safe(levels) -> bool:
    for i in range(len(levels)):
        _levels = [levels[j] for j in range(len(levels)) if j != i]
        if is_safe(_levels):
            return True
    return False


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


if __name__ == "__main__":
    main()
