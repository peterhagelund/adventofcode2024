#
# Based on Hyper Neutrino's walkthough of part 2: https://www.youtube.com/watch?v=SU6lp6wyd3I
#

import re

GATE = r'([a-z0-9]+) (AND|OR|XOR) ([a-z0-9]+) -> ([a-z0-9]+)'


def make_wire(char: str, number: int) -> str:
    return char + str(number).rjust(2, "0")


def verify_z(gates: dict[str, tuple[str, str, str]], wire: str, number: int) -> bool:
    # print("vz", wire, num)
    if wire not in gates:
        return False
    x, kind, y = gates[wire]
    if kind != "XOR":
        return False
    if number == 0:
        return sorted([x, y]) == ["x00", "y00"]
    return verify_intermediate_xor(gates, x, number) and verify_carry_bit(gates, y, number) or verify_intermediate_xor(gates, y, number) and verify_carry_bit(gates, x, number)


def verify_intermediate_xor(gates: dict[str, tuple[str, str, str]], wire: str, number: int) -> bool:
    # print("vx", wire, num)
    if wire not in gates:
        return False
    x, kind, y = gates[wire]
    if kind != "XOR":
        return False
    return sorted([x, y]) == [make_wire("x", number), make_wire("y", number)]


def verify_carry_bit(gates: dict[str, tuple[str, str, str]], wire: str, number: int) -> bool:
    # print("vc", wire, num)
    if wire not in gates:
        return False
    x, kind, y = gates[wire]
    if number == 1:
        if kind != "AND":
            return False
        return sorted([x, y]) == ["x00", "y00"]
    if kind != "OR":
        return False
    return verify_direct_carry(gates, x, number - 1) and verify_recarry(gates, y, number - 1) or verify_direct_carry(gates, y, number - 1) and verify_recarry(gates, x, number - 1)


def verify_direct_carry(gates: dict[str, tuple[str, str, str]], wire: str, number: int) -> bool:
    # print("vd", wire, num)
    if wire not in gates:
        return False
    x, kind, y = gates[wire]
    if kind != "AND":
        return False
    return sorted([x, y]) == [make_wire("x", number), make_wire("y", number)]


def verify_recarry(gates: dict[str, tuple[str, str, str]], wire: str, number: int) -> bool:
    # print("vr", wire, num)
    if wire not in gates:
        return False
    x, kind, y = gates[wire]
    if kind != "AND":
        return False
    return verify_intermediate_xor(gates, x, number) and verify_carry_bit(gates, y, number) or verify_intermediate_xor(gates, y, number) and verify_carry_bit(gates, x, number)


def verify(gates: dict[str, tuple[str, str, str]], number: int) -> bool:
    return verify_z(gates, make_wire("z", number), number)


def progress(gates: dict[str, tuple[str, str, str]]):
    i = 0
    while True:
        if not verify(gates, i):
            break
        i += 1
    return i


def main():
    gates: dict[str, tuple[str, str, str]] = {}
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            if line.isspace():
                break
        for line in f:
            matches = re.findall(GATE, line)
            if len(matches) > 0:
                x, kind, y, output = matches[0]
                gates[output] = (x, kind, y)

    def dump_wire(output: str, depth: int = 0) -> str:
        if output[0] in 'xy':
            return '  ' * depth + output
        x, kind, y = gates[output]
        return '  ' * depth + kind + ' (' + output + ')\n' + dump_wire(x, depth + 1) + '\n' + dump_wire(y, depth + 1)

    swaps = []

    for _ in range(4):
        baseline = progress(gates)
        for x in gates:
            for y in gates:
                if x == y:
                    continue
                gates[x], gates[y] = gates[y], gates[x]
                if progress(gates) > baseline:
                    break
                gates[x], gates[y] = gates[y], gates[x]
            else:
                continue
            break
        swaps += [x, y]
    print(f'answer = {",".join(sorted(swaps))}')


if __name__ == '__main__':
    main()
