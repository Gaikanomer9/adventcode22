
SCORE_SHAPE = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

SCORE_SHAPE_USUAL = {
    "A": 1,
    "B": 2,
    "C": 3
}

SCORE_RESULT = {
    -1: 0,
    0: 3,
    1: 6
}

# A, X rock
# B, Y paper
# C, Z scissors
#   A | B | C
# Z -1|  1| 0
# X  0| -1| 1
# Y  1|  0|-1

RESULTS_MAP = {
    "Z": {
        "A": -1, "B": 1, "C": 0
    },
    "X": {
        "A": 0, "B": -1, "C": 1
    },
    "Y": {
        "A": 1, "B": 0, "C": -1
    }
}

REVERSE_RESULTS = {
    "A": {
        "X": "C",
        "Y": "A",
        "Z": "B"
    },
    "B": {
        "X": "A",
        "Y": "B",
        "Z": "C"
    },
    "C": {
        "X": "B",
        "Y": "C",
        "Z": "A"
    }
}
RIGGED_RESULTS = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

# X - lose
# Y - draw
# Z - win
# A Y
# B X
# C Z
if __name__=="__main__":
    # with open("day2/input.txt") as file:
    #     strategy = file.readlines()
    #     total = 0
    #     for line in strategy:
    #         moves = line.replace("\n","").split(" ")
    #         result = RESULTS_MAP[moves[1]][moves[0]]
    #         points = SCORE_RESULT[result]
    #         points += SCORE_SHAPE[moves[1]]
    #         total += points
    #     print(total)
    #part2
    with open("day2/input.txt") as file:
        strategy = file.readlines()
        total = 0
        for line in strategy:
            moves = line.replace("\n","").split(" ")
            points = RIGGED_RESULTS[moves[1]]
            draw = REVERSE_RESULTS[moves[0]][moves[1]]
            points += SCORE_SHAPE_USUAL[draw]
            total += points
        print(total)

