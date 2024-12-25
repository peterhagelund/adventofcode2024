def main():
    towel_patterns: list[str] = []
    designs: list[str] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            line = line.strip()
            if len(towel_patterns) == 0:
                towel_patterns.extend([tp.strip() for tp in line.split(',')])
            elif len(line) == 0:
                continue
            else:
                designs.append(line)
    towel_patterns.sort(key=lambda tp: len(tp), reverse=True)
    cache: dict[str, int] = {}

    def count_design_possibilities(design: str) -> int:
        ld = len(design)
        if ld == 0:
            return 1
        if design in cache:
            return cache[design]
        count = 0
        for towel_pattern in towel_patterns:
            ltp = len(towel_pattern)
            if ltp <= ld and design[:ltp] == towel_pattern:
                count += count_design_possibilities(design[ltp:])
        cache[design] = count
        return count

    answer = 0
    for design in designs:
        count_design_possibilities(design)
        answer += cache[design]
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
