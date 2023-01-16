"""
Restructing the input so that it is in json form
for us to work with

"""

def monkey0_test (worry: int) -> int:
    return 1 if (worry % 13 == 0) else 7

def monkey1_test (worry: int) -> int:
    return 3 if (worry % 7 == 0) else 6

def monkey2_test (worry: int) -> int:
    return 5 if (worry % 3 == 0) else 4

def monkey3_test (worry: int) -> int:
    return 2 if (worry % 19 == 0) else 6

def monkey4_test (worry: int) -> int:
    return 0 if (worry % 5 == 0) else 5

def monkey5_test (worry: int) -> int:
    return 7 if (worry % 2 == 0) else 0

def monkey6_test (worry: int) -> int:
    return 2 if (worry % 11 == 0) else 4

def monkey7_test (worry: int) -> int:
    return 1 if (worry % 17 == 0) else 3

monkey_json = [
    {
        # Monkey 0
        'items': [71, 56, 50, 73],
        'operation': lambda x: x * 11,
        'test': monkey0_test
    },
    {
        # Monkey 1
        'items': [70, 89, 82],
        'operation': lambda x: x + 1,
        'test': monkey1_test
    },
    {
        # Monkey 2
        'items': [52, 95],
        'operation': lambda x: x * x,
        'test': monkey2_test
    },
    {
        # Monkey 3
        'items': [94, 64, 69, 87, 70],
        'operation': lambda x: x + 2,
        'test': monkey3_test
    },
    {
        # Monkey 4
        'items': [98, 72, 98, 53, 97, 51],
        'operation': lambda x: x + 6,
        'test': monkey4_test
    },
    {
        # Monkey 5
        'items': [79],
        'operation': lambda x: x + 7,
        'test': monkey5_test
    },
    {
        # Monkey 6
        'items': [77, 55, 63, 93, 66, 90, 88, 71],
        'operation': lambda x: x * 7,
        'test': monkey6_test
    },
    {
        # Monkey 7
        'items': [54, 97, 87, 70, 59, 82, 59],
        'operation': lambda x: x + 8,
        'test': monkey7_test
    }
]
