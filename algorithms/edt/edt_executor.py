from sklearn.model_selection import train_test_split

from algorithms.edt.EDT import EDT
import random
import numpy as np


def run_edt(a, b, h):
    random.seed(42)
    np.random.seed(42)

    mi, lambda_, target_h, tournament_k, mutation_prob = 245, 75, 10, 5, 0.0325

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

    x_train, x_test, y_train, y_test = train_test_split(a, b, test_size=0.33)

    tree.fit(x_train, y_train)
    accuracy = 1 - tree.eval(x_test, y_test)

    print(f'EDT Accuracy: {100 * accuracy:.3f}%')

