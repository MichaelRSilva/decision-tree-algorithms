import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from algorithms.cart.CART import CartTree
from config import algorithm_config
from utils.tree_util import check_accuracy


def run_cart(x: np.array, y: np.array, h: np.array):

    model = CartTree(
        criterion='gini',
        splitter='best'
    )
    model = model.fit(x, y)

    accuracy = check_accuracy(model, 5, x, y, h)
    print(f'CART Accuracy: {100 * accuracy:.3f}%')

    fig = plt.figure(figsize=(25, 20))
    _ = tree.plot_tree(
        model,
        feature_names=h,
        class_names=algorithm_config["cart"]["class_names"],
        filled=True
    )
    fig.savefig(algorithm_config["cart"]["path_output_image"])
