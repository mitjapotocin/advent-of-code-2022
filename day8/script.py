from data import data


def run():

    rows = data.split("\n")
    count = 0
    max_views = 0
    n_rows = len(rows)
    n_cols = len(rows[0])
    print(n_rows, n_cols)

    for index_row, row in enumerate(rows):
        for index_col, height in enumerate(row):
            if index_row == 0 or index_row == n_rows - 1 or index_col == 0 or index_col == n_cols - 1:
                count += 1
                continue

            not_visible_top = True
            for i in range(0, index_row):
                if i == index_row:
                    continue
                if rows[i][index_col] >= height:
                    not_visible_top = False
                    break

            not_visible_bottom = True
            for i in range(index_row, n_rows):
                if i == index_row:
                    continue
                if rows[i][index_col] >= height:
                    not_visible_bottom = False
                    break

            not_visible_left = True
            for i in range(0, index_col):
                if i == index_col:
                    continue
                if rows[index_row][i] >= height:
                    not_visible_left = False
                    break

            not_visible_right = True
            for i in range(index_col, n_cols):
                if i == index_col:
                    continue
                if rows[index_row][i] >= height:
                    not_visible_right = False
                    break

            if not_visible_top or not_visible_bottom or not_visible_left or not_visible_right:
                count += 1

            # part 2
            # go UP
            tree_visible_count_up = 0
            for i in reversed(range(0, index_row)):
                tree_visible_count_up += 1
                if rows[i][index_col] >= height:
                    break

            # go DOWN
            tree_visible_count_down = 0
            for i in range(index_row + 1, n_rows):
                tree_visible_count_down += 1
                if rows[i][index_col] >= height:
                    break

            # go leFT
            tree_visible_count_left = 0
            for i in reversed(range(0, index_col)):
                tree_visible_count_left += 1
                if rows[index_row][i] >= height:
                    break

            # go right
            tree_visible_count_right = 0
            for i in range(index_col + 1, n_cols):
                tree_visible_count_right += 1
                if rows[index_row][i] >= height:
                    break

            view_index = tree_visible_count_up * tree_visible_count_down * \
                tree_visible_count_left * tree_visible_count_right
            if view_index > max_views:
                max_views = view_index

    print(f"Answer 1: {count}")
    print(f"Answer 1: {max_views}")


if __name__ == "__main__":
    run()
