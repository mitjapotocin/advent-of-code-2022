from data import data


def get_stacks():
    rows = data.split("\n")

    stacks = []
    for _ in range(0, len(rows[0]), 4):
        stacks.append([])

    for row in rows:
        for index, i in enumerate(range(0, len(row), 4)):
            if i < len(row) and row[i] == "[":
                stacks[index].append(row[i + 1])

    return stacks


def run():
    stacks_pt1 = get_stacks()
    stacks_pt2 = get_stacks()

    rows = data.split("\n")

    # Part 1
    for row in rows:
        if row.startswith("move"):
            _, size_, _, from_, _, to_ = row.split(" ")
            size_ = int(size_)
            from_ = int(from_) - 1
            to_ = int(to_) - 1

            stacks_pt1[to_] = stacks_pt1[from_][:size_][::-1] + stacks_pt1[to_]
            stacks_pt1[from_] = stacks_pt1[from_][size_:]

    # Part 2
    for row in rows:
        if row.startswith("move"):
            _, size_, _, from_, _, to_ = row.split(" ")
            size_ = int(size_)
            from_ = int(from_) - 1
            to_ = int(to_) - 1

            stacks_pt2[to_] = stacks_pt2[from_][:size_] + stacks_pt2[to_]
            stacks_pt2[from_] = stacks_pt2[from_][size_:]
            

    answer1 = ""
    answer2 = ""
    
    for stack in stacks_pt1:
        answer1 = answer1 + stack[0];
    
    for stack in stacks_pt2:
        answer2 = answer2 + stack[0];
    
    
    print(f"Answer 1: {answer1}")
    print(f"Answer 2: {answer2}")
    


if __name__ == "__main__":
    run()
