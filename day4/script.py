from data import data

def print_range(range1, range2):
    string1 = ""
    string2 = ""
    for i in range(0, 100):
        string1 += "x" if (i == int(range1[0]) or i == int(range1[1])) else "."
        string2 += "x" if (i == int(range2[0]) or i == int(range2[1])) else "."
        
    print(string1)
    print(string2)
    print("---")

def run():
    # Pr1
    rows = data.split("\n")

    score = 0

    for row in rows:
        one, two = row.split(",")
        range1 = one.split("-")
        range2 = two.split("-")
        
        if int(range1[0]) >= int(range2[0]) and int(range1[1]) <= int(range2[1]):
            score = score + 1  
        elif int(range2[0]) >= int(range1[0]) and int(range2[1]) <= int(range1[1]):
            score = score + 1

    print("Pr1 score:")
    print(score)

    # Pr2
    score = 0
    
    for row in rows:
        one, two = row.split(",")
        range1 = one.split("-")
        range2 = two.split("-")

        overlap = set(range(int(range1[0]), int(range1[1]) + 1)) & set(range(int(range2[0]), int(range2[1]) + 1))
        print_range(range1, range2)
        score = score + 1 if len(overlap) > 0 else score
    
    print("Pr2 score:")
    print(score)


if __name__ == "__main__":
    run()
