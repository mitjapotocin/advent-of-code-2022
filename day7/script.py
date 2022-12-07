from data import data


def add_size_to_parent_folders(_disk, folder, size):
    if folder == "/":
        return

    parent_folder = ("-").join(folder.split("-")[:-1])
    _disk[parent_folder] += size

    add_size_to_parent_folders(_disk, parent_folder, size)


def run():
    disk = {}
    current_folder = []

    for row in data.split("\n"):
        if row.startswith("$"):
            if row.startswith("$ cd"):
                _, _, folder = row.split(" ")
                current_folder = current_folder[:-1] if folder == ".." else current_folder + [folder]
        else:
            if row.startswith("dir"):
                _, folder = row.split(" ")
                disk["-".join(current_folder + [folder])] = 0
            else:
                size, _ = row.split(" ")
                full_path = "-".join(current_folder)
                if disk.get(full_path):
                    disk[full_path] += int(size)
                else:
                    disk[full_path] = int(size)

    for folder in disk:
        size = disk[folder]
        if size != 0:
            add_size_to_parent_folders(disk, folder, size)

    folder_sum = 0

    for folder in disk:
        size = disk[folder]
        if size < 100000:
            folder_sum += size

    print(f"Answer 1: {folder_sum}")

    # Pt 2
    disc_occupied = disk["/"]
    target_size = 30000000 - 70000000 + disc_occupied

    the_chosen_one = float("inf")

    for folder in disk:
        size = disk[folder]
        if size < the_chosen_one and size > target_size:
            the_chosen_one = size
    
    print(f"Answer 2: {the_chosen_one}")

if __name__ == "__main__":
    run()
