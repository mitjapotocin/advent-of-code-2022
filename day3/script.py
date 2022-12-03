from data import data


def transformCharToNum(char: str):
    num = ord(char)

    if num > 96:
        return num - 96
    else:
        return num - 38


def run():
    # Pr1
    score = 0
    rows = data.split("\n")

    for row in rows:
        same_letter = None
        first_part, second_part = row[:len(row)//2], row[len(row)//2:]
        for letter in first_part:
            if letter in second_part:
                same_letter = letter

        score += transformCharToNum(same_letter)

    print("Pr1 score:")
    print(score)

    # Pr2
    score = 0
    list_of_3 = []

    for row in rows:
        list_of_3.append(row)

        if len(list_of_3) == 3:
            common = set(list_of_3[0]) & set(list_of_3[1]) & set(list_of_3[2])
            list_of_3 = []
            score += transformCharToNum(common.pop())

    print("Pr2 score:")
    print(score)


if __name__ == "__main__":
    run()
