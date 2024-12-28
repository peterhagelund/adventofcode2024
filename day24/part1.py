import re

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
    while len(gates) > 0:
        processed_gates: list[tuple[str, str, str, str]] = []
        for input1, kind, input2, output in gates:
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
                processed_gates.append((input1, kind, input2, output))
        gates = [g for g in gates if g not in processed_gates]
    z_wires = sorted([k for k in wires.keys() if k.startswith('z')])
    answer = 0
    count = 0
    for name in z_wires:
        value = wires[name]
        if value is True:
            answer |= 2**count
        count += 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
