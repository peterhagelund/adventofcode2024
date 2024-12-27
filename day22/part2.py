def next_random(number: int) -> int:
    number = (number ^ number << 6) % 16777216
    number = (number ^ number >> 5) % 16777216
    number = (number ^ number << 11) % 16777216
    return number


def calculate_sequence_map(number: int) -> dict[tuple[int, int, int, int], int]:
    sequence_map: dict[tuple[int, int, int, int], int] = {}
    last_price = number % 10
    prices: list[int] = []
    price_changes: list[int] = []
    for _ in range(2000):
        number = next_random(number)
        price = number % 10
        prices.append(price)
        price_changes.append(price - last_price)
        last_price = price
    for i in range(4, len(price_changes)):
        sequence = (price_changes[i - 3], price_changes[i - 2], price_changes[i - 1], price_changes[i])
        if sequence not in sequence_map:
            sequence_map[sequence] = prices[i]
    return sequence_map


def main():
    secret_numbers: list[int] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            secret_numbers.append(int(line.strip()))
    answer = 0
    sequence_maps: list[dict[tuple[int, int, int, int], int]] = []
    sequences: set[tuple[int, int, int, int]] = set()
    for secret_number in secret_numbers:
        sequence_map = calculate_sequence_map(secret_number)
        sequence_maps.append(sequence_map)
        for sequence in sequence_map.keys():
            sequences.add(sequence)
    for sequence in sequences:
        bananas = 0
        for sequence_map in sequence_maps:
            bananas += sequence_map.get(sequence, 0)
        if bananas > answer:
            answer = bananas
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
