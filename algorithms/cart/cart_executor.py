import numpy as np
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.model_selection import train_test_split

from algorithms.cart.CART import CartTree
from config import algorithm_config


def run_cart(x: np.array, y: np.array, h: np.array):
    model = CartTree(
        criterion='gini',
        splitter='best'
    )

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33)

    model.fit(x_train, y_train)
    accuracy = 1 - model.eval(x_test, y_test)

    print(f'\nCART Accuracy: {100 * accuracy:.3f}%')

    if algorithm_config["cart"]["plot"]:
        fig = plt.figure(figsize=(25, 20))
        _ = tree.plot_tree(
            model,
            feature_names=h,
            class_names=algorithm_config["cart"]["class_names"],
            filled=True
        )
        fig.savefig(algorithm_config["cart"]["path_output_image"])
