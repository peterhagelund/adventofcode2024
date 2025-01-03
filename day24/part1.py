import re
from collections import deque

WIRE = r'([a-z0-9]+): (\d)\s+'
GATE = r'([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)'


def main():
    wires: dict[str, bool] = {}
    gates: deque[tuple[str, str, str, str]] = deque()
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            matches = re.findall(WIRE, line)
            if len(matches) > 0:
                name = matches[0][0]
                wires[name] = matches[0][1] == '1'
            else:
                matches = re.findall(GATE, line)
                if len(matches) > 0:
                    gates.append(matches[0])
    while gates:
        input1, kind, input2, output = gates.popleft()
        if input1 in wires and input2 in wires:
            value1, value2 = wires[input1], wires[input2]
            match kind:
                case 'AND':
                    result = value1 & value2
                case 'OR':
                    result = value1 | value2
                case 'XOR':
                    result = value1 ^ value2
            wires[output] = result
        else:
            gates.append((input1, kind, input2, output))
    z_wires = sorted([k for k in wires.keys() if k.startswith('z')])
    answer = 0
    bit = 1
    for name in z_wires:
        if wires[name] is True:
            answer |= bit
        bit <<= 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
