from typing import List


class TuringMachine:

    def __init__(self, state, read_position: int):
        self.state = state
        self.current_read_position = read_position

    def operation(self):
        return self.state[self.current_read_position]

    def value(self, delta_to_read_position: int):
        position_of_value = self.state[self.current_read_position + delta_to_read_position]
        return self.state[position_of_value]

    def output_position(self):
        return self.state[self.current_read_position + 3]

    def tick(self):
        t = {1: lambda x, y: x + y,
             2: lambda x, y: x * y,
             }

        func = t[self.operation()]
        self.state[self.output_position()] = func(self.value(1), self.value(2))

        self.current_read_position += 4

    def continue_ticking(self) -> bool:
        return not self.operation() == 99

    def __str__(self):
        return f'{self.state} , {self.current_read_position}'


def turing(state: List) -> List:
    a = TuringMachine(state=state, read_position=0)

    while a.continue_ticking():
        a.tick()

    return a.state


if __name__ == '__main__':

    puzzle_state = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 9, 1, 19, 1, 19, 6, 23, 2, 6, 23, 27, 2, 27, 9,
                    31, 1, 5, 31, 35, 1, 35, 10, 39, 2, 39, 9, 43, 1, 5, 43, 47, 2, 47, 10, 51, 1, 51, 6, 55, 1, 5, 55,
                    59, 2, 6, 59, 63, 2, 63, 6, 67, 1, 5, 67, 71, 1, 71, 9, 75, 2, 75, 10, 79, 1, 79, 5, 83, 1, 10, 83,
                    87, 1, 5, 87, 91, 2, 13, 91, 95, 1, 95, 10, 99, 2, 99, 13, 103, 1, 103, 5, 107, 1, 107, 13, 111, 2,
                    111, 9, 115, 1, 6, 115, 119, 2, 119, 6, 123, 1, 123, 6, 127, 1, 127, 9, 131, 1, 6, 131, 135, 1, 135,
                    2, 139, 1, 139, 10, 0, 99, 2, 0, 14, 0]

    puzzle_state[1] = 12
    puzzle_state[2] = 2

    print(puzzle_state)
    print(turing(puzzle_state))