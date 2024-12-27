def next_random(number: int) -> int:
    number = (number ^ number << 6) % 16777216
    number = (number ^ number >> 5) % 16777216
    number = (number ^ number << 11) % 16777216
    return number


def main():
    secret_numbers: list[int] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            secret_numbers.append(int(line.strip()))
    answer = 0
    for secret_number in secret_numbers:
        for _ in range(2000):
            secret_number = next_random(secret_number)
        answer += secret_number
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
