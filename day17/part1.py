class Computer:
    def __init__(self, a: int, b: int, c: int, program: list[int]):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.program = program
        self.ip = 0
        self.output: list[int] = []

    def combo_operand(self, operand: int) -> int:
        assert operand != 7
        if operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c
        else:
            return operand

    def run(self):
        while self.ip < len(self.program):
            opcode = self.program[self.ip]
            operand = self.program[self.ip + 1]
            match opcode:
                case 0:  # adv
                    self.a = self.a >> self.combo_operand(operand)
                    self.ip += 2
                case 1:  # bxl
                    self.b = self.b ^ operand
                    self.ip += 2
                case 2:  # bst
                    self.b = self.combo_operand(operand) % 8
                    self.ip += 2
                case 3:  # jnz
                    if self.a != 0:
                        self.ip = operand
                    else:
                        self.ip += 2
                case 4:  # bxc
                    self.b = self.b ^ self.c
                    self.ip += 2
                case 5:  # out
                    self.output.append(self.combo_operand(operand) % 8)
                    self.ip += 2
                case 6:  # bdv
                    self.b = self.a >> self.combo_operand(operand)
                    self.ip += 2
                case 7:  # cdv
                    self.c = self.a >> self.combo_operand(operand)
                    self.ip += 2


def main():
    a = 0
    b = 0
    c = 0
    program: list[int] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            if line.startswith('Register A: '):
                a = int(line[12:])
            if line.startswith('Register B: '):
                b = int(line[12:])
            if line.startswith('Register C: '):
                c = int(line[12:])
            if line.startswith('Program: '):
                program.extend([int(i.strip()) for i in line[9:].split(',')])
    computer = Computer(a, b, c, program)
    computer.run()
    print(f'answer = {','.join(str(o) for o in computer.output)}')


if __name__ == '__main__':
    main()
