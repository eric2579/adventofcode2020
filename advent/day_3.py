# Day 3

def get_shape(path):
    with open(path, 'r') as f:
        ski_slope = [i.rstrip() for i in f]
    rows = len(ski_slope)
    cols = len(ski_slope[0])
    return rows, cols, ski_slope


def count_trees(path, horizontal_count, vertical_count):
    total_rows, total_cols, ski_slope = get_shape(path)
    tree_count = 0
    curr_col_idx = 0
    for curr_row_idx in range(vertical_count, total_rows, vertical_count):
        curr_col_idx += horizontal_count
        mod_col_idx = curr_col_idx % total_cols
        if ski_slope[curr_row_idx][mod_col_idx] == '#':
            tree_count += 1
    return tree_count


def count_trees_pt2(path, horizontal_list, vertical_list):
    total_multiplied_trees = 1
    for i, j in zip(horizontal_list, vertical_list):
        trees = count_trees(path, i, j)
        total_multiplied_trees *= trees
    return total_multiplied_trees


if __name__ == '__main__':
    print(count_trees('../resources/day_3.txt', horizontal_count=3, vertical_count=1))
    print(count_trees_pt2('../resources/day_3.txt', horizontal_list=[1, 3, 5, 7, 1], vertical_list=[1, 1, 1, 1, 2]))
