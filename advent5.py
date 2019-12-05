import itertools
from typing import List

from collections import namedtuple

instruction = namedtuple('instruction', 'opcode parametercount function')


class TuringMachine:

    def __init__(self, state, read_position: int = 0):
        self.state = state
        self.current_read_position = read_position
        self.machine_input = None
        self.output = None

    def read_position_value(self):
        return self.state[self.current_read_position]

    def current_operation(self):
        w = {1: instruction(opcode=1,
                            parametercount=3,
                            function=self.adding,
                            ),
             2: instruction(opcode=2,
                            parametercount=3,
                            function=self.multiplying,
                            ),
             3: instruction(opcode=3,
                            parametercount=1,
                            function=self.storeinput,
                            ),
             4: instruction(opcode=4,
                            parametercount=1,
                            function=self.getoutput,
                            ),

             }
        return w[self.operation()]

    def operation(self):
        value_at_read_position = self.state[self.current_read_position]
        print(value_at_read_position)
        o = abs(value_at_read_position) % 100  # to get the last 2 digits
        print(o)
        return o

    def adding(self, listie):
        mempos_value_1 = listie[0]
        mempos_value_2 = listie[1]
        mempos_ouput = listie[2]

        value_1 = self.state[mempos_value_1]
        value_2 = self.state[mempos_value_2]

        self.state[mempos_ouput] = value_1 + value_2

    def multiplying(self):
        p = self.parameters()

        mempos_value_1 = p[0][0]
        mempos_value_2 = p[1][0]
        mempos_ouput = p[2][0]

        value_1 = self.state[mempos_value_1] if p[0][1] == 0 else p[0][0]
        value_2 = self.state[mempos_value_2] if p[1][1] == 0 else p[1][0]

        self.state[mempos_ouput] = value_1 * value_2

    def storeinput(self, listie):
        mempos = listie[0]
        self.state[mempos] = self.machine_input

    def getoutput(self, listie):
        mempos = listie[0]
        self.output = self.state[mempos]

    def value(self, delta_to_read_position: int):
        position_of_value = self.state[self.current_read_position + delta_to_read_position]
        return self.state[position_of_value]

    def output_position(self):
        return self.state[self.current_read_position + 3]

    def tick(self):
        w = {1: instruction(opcode=1,
                            parametercount=3,
                            function=self.adding,
                            ),
             2: instruction(opcode=2,
                            parametercount=3,
                            function=self.multiplying,
                            ),
             3: instruction(opcode=3,
                            parametercount=1,
                            function=self.storeinput,
                            ),
             4: instruction(opcode=4,
                            parametercount=1,
                            function=self.getoutput,
                            ),

             }
        print(f'my state {self.state}')
        print(f"current read position is {self.current_read_position}")
        print(f'my state {self.state}')
        print(f'the self.operation is {self.operation()}')
        print(f'my state {self.state}')
        i = w[self.operation()]
        print(f'the operation is {i}')
        start = self.current_read_position + 1
        stop = start + i.parametercount
        listie = self.state[start: stop]
        print('this is listie')
        print(listie)
        i.function()

        self.current_read_position += (i.parametercount + 1)

    def parameters(self):
        start = self.current_read_position + 1
        stop = start + self.current_operation().parametercount
        listie = self.state[start: stop]

        a = itertools.zip_longest(listie, self.parameter_modes(), fillvalue=0)
        e = list()
        for w in a:
            e.append(w)

        return e

    def parameter_modes(self):
        a = str(self.read_position_value())[:-2]
        b = a[::-1]

        return [int(u) for u in b]

    #   print(f"current read position is {self.current_read_position}")

    def continue_ticking(self) -> bool:
        return not self.operation() == 99

    def run(self, machine_input=None):
        self.machine_input = machine_input

        while self.continue_ticking():
            print(f'my state {self.state}')
            print(f"current read position is {self.current_read_position}")
            self.tick()

        return self.output

    def __str__(self):
        return f'{self.state} , {self.current_read_position}'


if __name__ == '__main__':
    s = [1, 1, 1, 4, 99, 5, 6, 0, 99]
    state = [1002, 4, 3, 4, 33]
    e = TuringMachine(state=state)

    print(e.parameters())
    print(e.operation())
    e.run()

    #

    puzzle_input = [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1102, 57, 23, 224, 101, -1311, 224, 224, 4, 224,
                    1002, 223, 8, 223, 101, 6, 224, 224, 1, 223, 224, 223, 1102, 57, 67, 225, 102, 67, 150, 224, 1001,
                    224, -2613, 224, 4, 224, 1002, 223, 8, 223, 101, 5, 224, 224, 1, 224, 223, 223, 2, 179, 213, 224,
                    1001, 224, -469, 224, 4, 224, 102, 8, 223, 223, 101, 7, 224, 224, 1, 223, 224, 223, 1001, 188, 27,
                    224, 101, -119, 224, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 7, 224, 1, 223, 224, 223, 1, 184,
                    218, 224, 1001, 224, -155, 224, 4, 224, 1002, 223, 8, 223, 1001, 224, 7, 224, 1, 224, 223, 223,
                    1101, 21, 80, 224, 1001, 224, -101, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 1, 224, 1, 224, 223,
                    223, 1101, 67, 39, 225, 1101, 89, 68, 225, 101, 69, 35, 224, 1001, 224, -126, 224, 4, 224, 1002,
                    223, 8, 223, 1001, 224, 1, 224, 1, 224, 223, 223, 1102, 7, 52, 225, 1102, 18, 90, 225, 1101, 65, 92,
                    225, 1002, 153, 78, 224, 101, -6942, 224, 224, 4, 224, 102, 8, 223, 223, 101, 6, 224, 224, 1, 223,
                    224, 223, 1101, 67, 83, 225, 1102, 31, 65, 225, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1,
                    99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1,
                    99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999,
                    1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 1007,
                    226, 226, 224, 102, 2, 223, 223, 1005, 224, 329, 1001, 223, 1, 223, 108, 677, 226, 224, 1002, 223,
                    2, 223, 1005, 224, 344, 1001, 223, 1, 223, 1007, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 359,
                    1001, 223, 1, 223, 1107, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 374, 1001, 223, 1, 223, 8, 226,
                    677, 224, 1002, 223, 2, 223, 1006, 224, 389, 101, 1, 223, 223, 8, 677, 677, 224, 102, 2, 223, 223,
                    1006, 224, 404, 1001, 223, 1, 223, 1008, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 419, 1001, 223,
                    1, 223, 107, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 434, 101, 1, 223, 223, 7, 226, 226, 224,
                    1002, 223, 2, 223, 1005, 224, 449, 1001, 223, 1, 223, 1107, 226, 226, 224, 1002, 223, 2, 223, 1006,
                    224, 464, 1001, 223, 1, 223, 1107, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 479, 1001, 223, 1,
                    223, 8, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 494, 1001, 223, 1, 223, 1108, 226, 677, 224,
                    1002, 223, 2, 223, 1006, 224, 509, 101, 1, 223, 223, 1008, 677, 677, 224, 1002, 223, 2, 223, 1006,
                    224, 524, 1001, 223, 1, 223, 1008, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 539, 1001, 223, 1,
                    223, 1108, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 554, 101, 1, 223, 223, 108, 677, 677, 224,
                    102, 2, 223, 223, 1006, 224, 569, 101, 1, 223, 223, 1108, 677, 226, 224, 102, 2, 223, 223, 1005,
                    224, 584, 1001, 223, 1, 223, 108, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 599, 1001, 223, 1,
                    223, 1007, 226, 677, 224, 102, 2, 223, 223, 1005, 224, 614, 1001, 223, 1, 223, 7, 226, 677, 224,
                    102, 2, 223, 223, 1006, 224, 629, 1001, 223, 1, 223, 107, 226, 226, 224, 102, 2, 223, 223, 1005,
                    224, 644, 101, 1, 223, 223, 7, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 659, 101, 1, 223, 223,
                    107, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 674, 1001, 223, 1, 223, 4, 223, 99, 226]
