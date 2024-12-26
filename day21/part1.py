from collections import deque
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
    # print(find_possible_sequences('029A', numberic_sequences))
    answer = 0
    for door_code in door_codes:
        next_sequences = find_possible_sequences(door_code, numberic_sequences)
        for _ in range(2):
            possible_next_sequences: list[list[str]] = []
            for ns in next_sequences:
                possible_next_sequences.extend(find_possible_sequences(ns, directional_sequences))
            shortest = min(map(len, possible_next_sequences))
            next_sequences = [pns for pns in possible_next_sequences if len(pns) == shortest]
        answer += len(next_sequences[0]) * int(door_code[:-1])
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
