def can_be_made_true(test_value: int, numbers: list[int]) -> bool:
    results = [numbers[0]]
    for i in range(1, len(numbers)):
        n = numbers[i]
        _results: list[int] = []
        for r in results:
            for o in ['*', '+']:
                match o:
                    case '*':
                        result = r * n
                    case '+':
                        result = r + n
                if result <= test_value:
                    _results.append(result)
        if len(_results) == 0:
            return False
        results = _results
    for r in results:
        if r == test_value:
            return True
    return False


def main():
    answer = 0
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            parts = line.strip().split(':')
            test_value = int(parts[0].strip())
            numbers = [int(n) for n in parts[1].strip().split()]
            if can_be_made_true(test_value, numbers):
                answer += test_value
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
