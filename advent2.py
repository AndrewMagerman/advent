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
        return f'|{self.state} , {self.current_read_position}'


def turing(state: List) -> List:
    a = TuringMachine(state=state, read_position=0)

    while a.continue_ticking():
        a.tick()

    return a.state


if __name__ == '__main__':
    print(turing([1, 0, 0, 0, 99]))
    # print(len(all_module_masses))
    # print(fuel_for_trip())
    # print(fuel_for_trip_with_fuel_eigenbedarf())
