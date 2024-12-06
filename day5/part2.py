from functools import cmp_to_key


def can_come_before(page1: int, page2: int, rules: set[tuple[int, int]]) -> bool:
    if (page1, page2) in rules:
        return True
    if (page2, page1) in rules:
        return False
    return True


def can_come_after(page1: int, page2: int, rules: set[tuple[int, int]]) -> bool:
    if (page2, page1) in rules:
        return True
    if (page1, page2) in rules:
        return False
    return True


def is_in_right_order(update: list[int], rules: set[tuple[int, int]]) -> bool:
    for i in range(len(update)):
        page1 = update[i]
        for j in range(len(update)):
            if j == i:
                continue
            page2 = update[j]
            if i < j:
                if not can_come_before(page1, page2, rules):
                    return False
            else:
                if not can_come_after(page1, page2, rules):
                    return False
    return True


def main():
    rules: set[tuple[int, int]] = set()
    updates: list[list[int]] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            if len(line) < 2:
                continue
            if line[2] == '|':
                rule = (int(line[0:2]), int(line[3:5]))
                rules.add(rule)
            else:
                update = [int(p) for p in line.strip().split(',')]
                assert len(update) % 2 == 1
                updates.append(update)
    answer = 0
    for update in updates:
        if is_in_right_order(update, rules):
            continue

        def rule_cmp(page1: int, page2: int) -> int:
            if can_come_after(page1, page2, rules):
                return 1
            elif can_come_before(page1, page2, rules):
                return -1
            else:
                return 0

        update.sort(key=cmp_to_key(rule_cmp))
        middle_page = update[len(update) // 2]
        answer += middle_page
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
