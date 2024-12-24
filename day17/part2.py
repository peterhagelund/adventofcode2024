def main():
    program: list[int] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            if line.startswith('Program: '):
                program.extend([int(i.strip()) for i in line[9:].split(',')])

    def find_a(target: list[int], answer: int) -> int:
        if len(target) == 0:
            return answer
        for i in range(8):
            a = answer << 3 | i
            b = 0
            c = 0
            output = None

            def combo_operand(operand: int) -> int:
                assert operand != 7
                if operand == 4:
                    return a
                elif operand == 5:
                    return b
                elif operand == 6:
                    return c
                else:
                    return operand

            for ip in range(0, len(program) - 2, 2):
                opcode = program[ip]
                operand = program[ip + 1]
                match opcode:
                    case 0:  # adv
                        pass  # we're hsndling this through the search
                    case 1:  # bxl
                        b = b ^ operand
                    case 2:  # bst
                        b = combo_operand(operand) % 8
                    case 3:  # jnz
                        pass  # we're not concerned with the JNZ instruction
                    case 4:  # bxc
                        b = b ^ c
                    case 5:  # out
                        output = combo_operand(operand) % 8
                    case 6:  # bdv
                        b = a >> combo_operand(operand)
                    case 7:  # cdv
                        c = a >> combo_operand(operand)
                if output == target[-1]:
                    _a = find_a(target[:-1], a)
                    if _a is None:
                        continue
                    return _a

    answer = find_a(program, 0)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
