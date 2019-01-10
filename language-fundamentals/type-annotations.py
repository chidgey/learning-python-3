#!/usr/bin/env python3

"""Type annotations are new in Python 3.6. Use them to hint what types to use.False

    Use types to prevent issues in larger code bases and reduce errors. It
    seems dynamic languages have a little feature envy to strongly typed
    languages like C# and Java after all.

    https://docs.python.org/3/glossary.html#term-type-hint
"""

from typing import Dict, List, Tuple

# A dictionary where the keys are strings and the values are ints
name_counts: Dict[str, int] = {
    "Adam": 5,
    "Chidgey": 20
}

# A list of integers
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# A list that holds dictionaries
list_of_dictionaries: List[Dict[str, int]] = [
    {"key1": 1},
    {"key2": 2}
]

my_data: Tuple[str, int, float] = ("Adam", 10, 30.5)

# interesting use of aliases for complex types just by assigning them a new name
LatLngVector = List[Tuple[float, float]]
points: LatLngVector = [
    (25.91375, -60.15503),
    (-11.01983, -166.48477),
    (-11.01983, -166.48477)
]


# Example of a type hint annotation to signal the type returned to the caller.
def sum_two_numbers(a: int, b: int) -> int:
    return a + b


# String based usage of annotations
def concat_two_strings(a: str, b: str) -> str:
    return a + b


# Examples of using type hints with variables
myRunningSum: int = sum_two_numbers(1, 3)
myMessage: str = concat_two_strings("hello", "world")

print(name_counts)
print(numbers)
print(my_data)
print(points)
print(myRunningSum)
print(myMessage)
