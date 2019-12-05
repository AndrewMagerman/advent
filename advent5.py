from typing import List

from collections import namedtuple

instruction = namedtuple('instruction', 'opcode parametercount function')


class TuringMachine:

    def __init__(self, state, read_position: int = 0):
        self.state = state
        self.current_read_position = read_position
        self.machine_input = None

    def operation(self):
        return self.state[self.current_read_position]

    # def parameters_current_instruction(self) -> List:
    #     ins = w[self.operation()]
    #     listie = self.state[self.operation(): ins.parametercount + 1]
    #     listie.reverse()
    #
    #     return listie

    # @classmethod
    def adding(self, listie):
        stack = self.parameters_current_instruction()

        pointer_value_1 = listie[0]
        pointer_value_2 = listie[1]
        pointer_ouput = listie[2]

        self.state[self.state[pointer_ouput]] = self.state[self.state[pointer_value_1]] + self.state[
            self.state[pointer_value_2]]

    def value(self, delta_to_read_position: int):
        position_of_value = self.state[self.current_read_position + delta_to_read_position]
        return self.state[position_of_value]

    def output_position(self):
        return self.state[self.current_read_position + 3]

    def tick(self):
        t = {1: lambda x, y: x + y,
             2: lambda x, y: x * y,
             }

        w = {1: instruction(opcode=1,
                            parametercount=3,
                            function=self.adding,
                            ),
             2: instruction(opcode=2,
                            parametercount=3,
                            function=self.adding,
                            ),

             }

        i = w[self.operation()]
        listie = self.state[self.operation(): i.parametercount + 1]
        i.function(listie)

        # parameters = self.state[self.operation(): i.parametercount]
        #
        # func = t[self.operation()]
        # self.state[self.output_position()] = func(self.value(1), self.value(2))

        self.current_read_position += (i.parametercount + 1)

    def continue_ticking(self) -> bool:
        return not self.operation() == 99

    def run(self, machine_input=None):
        self.machine_input = machine_input

        while self.continue_ticking():
            self.tick()

        return 19

    def __str__(self):
        return f'{self.state} , {self.current_read_position}'


if __name__ == '__main__':
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
