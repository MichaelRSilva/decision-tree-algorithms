import numpy as np

from algorithms.brute.BruteNode import BruteNode
from algorithms.brute.brute_tree_util import build_tree, print_min_tree
from config import algorithm_config
from utils.collection_util import get_data_permutations
from utils.dataset_util import split


def run_brute(x, header):
    value_true = algorithm_config["brute"]["value_true"]
    value_false = algorithm_config["brute"]["value_false"]
    max_cols = algorithm_config["brute"]["max_cols"]
    max_data = algorithm_config["brute"]["max_data"]

    target = (x[:, -1])[:max_data]
    x = x[:, :max_cols][:max_data]
    x = (np.c_[x, target]).tolist()

    h = header[:max_cols]
    h.append(header[-1])
    index_results = len(h) - 1
    permutations = get_data_permutations(x, h)
    dataset = permutations[0]
    metas = permutations[1]

    trees = []

    for i, matrix in enumerate(list(dataset)):
        split_matrix = split(matrix, 0, value_true)
        root = BruteNode(
            metas[i][0],
            left=build_tree(split_matrix[0], 1, value_true, metas[i], index_results, value_false),
            right=build_tree(split_matrix[1], 1, value_true, metas[i], index_results, value_false)
        )
        trees.append(root)

    if algorithm_config["brute"]["print"]:
        print_min_tree(trees)
