import re
from collections import deque

WIRE = r'([a-z0-9]+): (\d)\s+'
GATE = r'([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)'


def main():
    wires: dict[str, bool] = {}
    gates: list[tuple[str, str, str, str]] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            matches = re.findall(WIRE, line)
            if len(matches) > 0:
                name = matches[0][0]
                value = matches[0][1] == '1'
                wires[name] = value
            else:
                matches = re.findall(GATE, line)
                if len(matches) > 0:
                    gates.append(matches[0])
    queue: deque[tuple[str, str, str, str]] = deque(gates)
    while queue:
        input1, kind, input2, output = queue.popleft()
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
            queue.append((input1, kind, input2, output))
    answer = 0
    numbers: list[int] = []
    for c in 'xyz':
        c_wires = sorted([k for k in wires.keys() if k.startswith(c)])
        number = 0
        bit = 1
        for name in c_wires:
            value = wires[name]
            if value is True:
                number |= bit
            bit <<= 1
        numbers.append(number)

    print(f'x =  {numbers[0]:b}')
    print(f'y =  {numbers[1]:b}')
    print(f'z = {numbers[2]:b}')
    print(f'x + y = {numbers[0] + numbers[1]}')
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
