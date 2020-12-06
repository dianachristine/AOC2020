import math
from data import get_data_from_fail


def get_bigger_map(treemap, n: int):
    return [treemap[i] * n for i in range(len(treemap))]


def find_n(map, r_step, d_step):
    return math.ceil(len(map) / (len(map[0]) // r_step)) * d_step


def find_num_of_encountered_trees(treemap, r_step, d_step) -> int:
    trees = 0
    step = r_step
    for i in range(d_step, len(treemap), d_step):
        if treemap[i][r_step] == '#':
            trees += 1
        r_step += step
    return trees


if __name__ == '__main__':
    data = get_data_from_fail("data.txt", "\n")

    right_step = 3
    down_step = 1
    num_of_trees1 = find_num_of_encountered_trees(get_bigger_map(data, find_n(data, right_step, down_step)), right_step, down_step)
    print(num_of_trees1)  # 218

    right_step = 1
    down_step = 1
    num_of_trees2 = find_num_of_encountered_trees(get_bigger_map(data, find_n(data, right_step, down_step)), right_step, down_step)

    right_step = 5
    down_step = 1
    num_of_trees3 = find_num_of_encountered_trees(get_bigger_map(data, find_n(data, right_step, down_step)), right_step, down_step)

    right_step = 7
    down_step = 1
    num_of_trees4 = find_num_of_encountered_trees(get_bigger_map(data, find_n(data, right_step, down_step)), right_step, down_step)

    right_step = 1
    down_step = 2
    num_of_trees5 = find_num_of_encountered_trees(get_bigger_map(data, find_n(data, right_step, down_step)), right_step, down_step)

    print(num_of_trees1 * num_of_trees2 * num_of_trees3 * num_of_trees4 * num_of_trees5)  # 3847183340
