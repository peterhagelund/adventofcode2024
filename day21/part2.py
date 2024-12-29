from collections import deque
from functools import cache
from itertools import product
from sys import maxsize

NUMERIC_KEYPAD = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A'],
]

DIRECTIONAL_KEYPAD = [
    [' ', '^', 'A'],
    ['<', 'v', '>'],
]

MOVES = [
    (-1, 0, '^'),
    (1, 0, 'v'),
    (0, -1, '<'),
    (0, 1, '>'),
]


def compute_keypad_sequences(keypad: list[list[str]]) -> dict[tuple[str, str], str]:
    positions: dict[str, tuple[int, int]] = {}
    for y in range(len(keypad)):
        for x in range(len(keypad[y])):
            if keypad[y][x] != ' ':
                positions[keypad[y][x]] = (y, x)
    sequences: dict[tuple[str, str], str] = {}
    for key1 in positions:
        for key2 in positions:
            if key1 == key2:
                sequences[(key1, key2)] = 'A'
                continue
            possible_sequences: list[str] = []
            queue: deque[tuple[tuple[int, int], str]] = deque([(positions[key1], '')])
            optimal = maxsize
            while queue:
                (y, x), keys = queue.popleft()
                for move in MOVES:
                    _y, _x, key = y + move[0], x + move[1], move[2]
                    if _y < 0 or _y >= len(keypad) or _x < 0 or _x >= len(keypad[0]):
                        continue
                    if keypad[_y][_x] == ' ':
                        continue
                    if keypad[_y][_x] == key2:
                        if optimal < len(keys) + 1:
                            break
                        optimal = len(keys) + 1
                        possible_sequences.append(keys + key + 'A')
                    else:
                        queue.append(((_y, _x), keys + key))
                else:
                    continue
                break
            sequences[(key1, key2)] = possible_sequences
    return sequences


def find_possible_sequences(keys: str, sequences: dict[tuple[str, str], str]) -> list[str]:
    options = [sequences[(k1, k2)] for k1, k2 in zip('A' + keys, keys)]
    return [''.join(p) for p in product(*options)]


def main():
    door_codes: list[int] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            door_codes.append(line.strip())
    numberic_sequences = compute_keypad_sequences(NUMERIC_KEYPAD)
    directional_sequences = compute_keypad_sequences(DIRECTIONAL_KEYPAD)
    directional_lengths = {k: len(v[0]) for k, v in directional_sequences.items()}

    @cache
    def compute_length(key1: str, key2: str, depth: int) -> int:
        if depth == 1:
            return directional_lengths[(key1, key2)]
        min_length = maxsize
        for sequence in directional_sequences[(key1, key2)]:
            length = 0
            for _key1, _key2 in zip('A' + sequence, sequence):
                length += compute_length(_key1, _key2, depth - 1)
            min_length = min(min_length, length)
        return min_length

    answer = 0
    for door_code in door_codes:
        next_sequences = find_possible_sequences(door_code, numberic_sequences)
        min_length = maxsize
        for sequence in next_sequences:
            length = 0
            for key1, key2 in zip('A' + sequence, sequence):
                length += compute_length(key1, key2, 25)
            min_length = min(min_length, length)
        answer += min_length * int(door_code[:-1])
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
