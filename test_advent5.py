import pytest

from advent5 import TuringMachine


def turing(state):
    e = TuringMachine(state=state)
    e.run()
    return e.state


def t2(state, input):
    e = TuringMachine(state=state)
    return e.run(machine_input=input)


def test_turing_machine_add():
    e = TuringMachine(state=[1, 0, 0, 0, 99])
    e.run()
    assert e.state == [2, 0, 0, 0, 99]


def test_mult():
    assert turing([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert turing([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]


def test_turing_machine_mystery():
    assert turing([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def test_input():
    assert t2([3, 0, 4, 0, 99], 1) == 1
    assert t2([3, 0, 4, 0, 99], 100) == 100


def test_mult1():
    assert turing([1002, 4, 3, 4, 33]) == [1002, 4, 3, 4, 99]

@pytest.fixture
def prep():
    state = [1002, 4, 3, 4, 33]
    return TuringMachine(state=state)

def test_p(prep):
    assert prep.operation() == 2

def test_i(prep):
    assert prep.parameter_modes() == [0, 1]

def test_l(prep):
    assert prep.parameters() == [(4, 0), (3, 1), (4, 0)]


# def test_param():
#     e = TuringMachine(state=[1, 0, 0, 0, 99])
#     assert e.parameters_current_instruction() == [0, 0, 0]
#
#     e2 = TuringMachine(state=[1, 1, 2, 3, 99])
#     assert e2.parameters_current_instruction() == [3, 2, 1]


if __name__ == '__main__':
    pass
