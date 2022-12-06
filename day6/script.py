from data import data

def run():

    # Part 1
    for index in enumerate(data):
        marker = data[index:index+4]
        if len(set(marker)) == 4:
            print("Answer1: " + index + 4)
            break
    
    # Part 2
    for index in enumerate(data):
        marker = data[index:index+14]
        if len(set(marker)) == 14:
            print("Answer2: " + index + 14)
            break

    


if __name__ == "__main__":
    run()
