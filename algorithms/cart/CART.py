from sklearn import tree
import numpy as np


class CartTree(tree.DecisionTreeClassifier):
    def eval(self, predict_set: np.ndarray, predict_train: np.ndarray) -> float:
        predicts = self.predict(predict_set)
        errors = predicts != predict_train

        return errors.sum() / len(errors)
