# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.
from advent1 import fuel, fuel_with_fuel_mass_included
from advent2 import turing, computer
from advent3 import manhattan_distance_closest_intersection, steps_closest
from advent4 import isvalid


def test_fuel():
    assert fuel(12) == 2
    assert fuel(14) == 2
    assert fuel(1969) == 654
    assert fuel(100756) == 33583


# A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.
# At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
# The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.

def test_fuel_with_fuel_mass():
    assert fuel_with_fuel_mass_included(14) == 2
    assert fuel_with_fuel_mass_included(1969) == 966
    assert fuel_with_fuel_mass_included(100756) == 50346


def test_turing_machine_add():
    assert turing([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]


def test_turing_machine_multiply():
    assert turing([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert turing([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]


def test_turing_machine_mystery():
    assert turing([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def test_computer():
    assert computer(noun=12, verb=2) == 6730673
    assert computer(noun=12, verb=2) == 6730673


test_wire_1A = "R8,U5,L5,D3"
test_wire_1B = "U7,R6,D4,L4"

test_wire_2A = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
test_wire_2B = "U62,R66,U55,R34,D71,R55,D58,R83"

test_wire_3A = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
test_wire_3B = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"


def test_man_1():
    assert manhattan_distance_closest_intersection(test_wire_1A, test_wire_1B) == 6
    assert manhattan_distance_closest_intersection(test_wire_2A, test_wire_2B) == 159
    assert manhattan_distance_closest_intersection(test_wire_3A, test_wire_3B) == 135

def test_man_2():
    assert steps_closest(test_wire_1A, test_wire_1B) == 30
    assert steps_closest(test_wire_2A, test_wire_2B) == 610
    assert steps_closest(test_wire_3A, test_wire_3B) == 410

def test_password_validator():
    assert not isvalid("0")
    assert not isvalid("00")
    assert not isvalid("0000")
    assert not isvalid("00000")
    assert not isvalid("0000000")
    assert not isvalid("123456")
    assert  isvalid("111111")
    assert not isvalid("223450")
    assert not isvalid("123789")



if __name__ == '__main__':
    pass
