"""Levels

Example level:
LEVELX = [
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1],
]
"""

import copy


LEVEL1 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

LEVEL2 = [
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
]

LEVEL3 = [
    [0, 1, 0, 1, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 1, 0],
]

LEVEL4 = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
]

LEVEL5 = [
    [1, 1, 1, 1, 0],
    [1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1],
]

LEVEL6 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [0, 1, 1, 1, 0],
]

LEVEL7 = [
    [1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 0],
]

LEVEL8 = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
]

LEVEL9 = [
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 0, 0],
]

LEVEL10 = [
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

LEVELS = [
    LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5,
    LEVEL6, LEVEL7, LEVEL8, LEVEL9, LEVEL10,
]

EMPTY = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]

ANIMATION = []

STEPS = [
    [0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
    [1, 4], [2, 4], [3, 4], [4, 4], [4, 3],
    [4, 2], [4, 1], [4, 0], [3, 0], [2, 0],
    [1, 0], [1, 1], [1, 2], [1, 3], [2, 3],
    [3, 3], [3, 2], [3, 1], [2, 1], [2, 2],
]

for item in STEPS:
    board = copy.deepcopy(EMPTY)
    board[item[0]][item[1]] = 1
    ANIMATION.append(board)

