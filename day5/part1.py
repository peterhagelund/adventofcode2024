def can_come_before(page1: int, page2: int, rules: list[tuple[int, int]]) -> bool:
    for rule in rules:
        if rule[0] == page1 and rule[1] == page2:
            return True
        if rule[0] == page2 and rule[1] == page1:
            return False
    return True


def can_come_after(page1: int, page2: int, rules: list[tuple[int, int]]) -> bool:
    for rule in rules:
        if rule[0] == page2 and rule[1] == page1:
            return True
        if rule[0] == page1 and rule[1] == page2:
            return False
    return True


def is_in_right_order(update: list[int], rules: list[tuple[int, int]]) -> bool:
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
    rules: list[tuple[int, int]] = []
    updates: list[list[int]] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            if len(line) < 2:
                continue
            if line[2] == '|':
                rule = (int(line[0:2]), int(line[3:5]))
                rules.append(rule)
            else:
                update = [int(p) for p in line.strip().split(',')]
                assert len(update) % 2 == 1
                updates.append(update)
    answer = 0
    for update in updates:
        if is_in_right_order(update, rules):
            middle_page = update[len(update) // 2]
            answer += middle_page
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()