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
    seen: set[str] = set()

    def can_make_design(design: str) -> bool:
        ld = len(design)
        if ld == 0:
            return True
        if design in seen:
            return False
        for towel_pattern in towel_patterns:
            ltp = len(towel_pattern)
            if ltp <= ld and design[:ltp] == towel_pattern:
                if can_make_design(design[ltp:]):
                    return True
                else:
                    seen.add(design)
        return False

    answer = 0
    for design in designs:
        print(design)
        seen.clear()
        if can_make_design(design):
            answer += 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
