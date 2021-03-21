from algorithms.edt.EDT import EDT
from utils.input_util import read_data
from utils.tree_util import check_accuracy
import random
import numpy as np


def run_edt():
    random.seed(42)
    np.random.seed(42)

    x, y, header = read_data()
    mi, lambda_, target_h, tournament_k, mutation_prob = 245, 75, 10, 5, 0.0325
    print(f'{mi}, {lambda_}, {target_h}, {tournament_k}, {mutation_prob:.4f}')

    tree = EDT(
        mi=mi,
        lambda_=lambda_,
        p_split=0.5,
        target_height=target_h,
        tournament_k=tournament_k,
        mutation_prob=mutation_prob,
        max_iter=500,
        stall_iter=100
    )

    accuracy, root = check_accuracy(tree, 5, x, y)
    print(f'EDT Accuracy: {100 * accuracy:.3f}%\n')

    tree.show(root, header=header)
