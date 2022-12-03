import data
data = data.total

elementsScore = {
    "X": 0,  # Rock 1
    "Y": 3,  # Paper 2
    "Z": 6,  # Scissors 3

    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
}

elementsScore2 = {
    "A": {
        "X": 3,
        "Y": 1,
        "Z": 2,
    },
    "B": {
        "X": 1,
        "Y": 2,
        "Z": 3,
    },
    "C": {
        "X": 2,
        "Y": 3,
        "Z": 1,
    }
}


def run():
    row = data.split("\n")
    score = 0
    for i in row:
        him = i[0]
        me = i[2]
        score = score + elementsScore[me] + elementsScore2[him][me]

            

    print(score)


if __name__ == "__main__":
    run()
