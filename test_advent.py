# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.
from advent1 import fuel, fuel_with_fuel_mass_included
from advent2 import turing, computer


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

if __name__ == '__main__':
    pass
