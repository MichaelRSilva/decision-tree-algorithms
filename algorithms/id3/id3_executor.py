import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from algorithms.id3.ID3 import GadId3Classifier


def run_id3(a, b, h):
    df = pd.DataFrame(np.c_[a, b])
    df.columns = h
    target = h[-1]

    # organize data into input and outputs
    x = df.drop(columns=target)
    y = df[target]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33)

    # initialize and fit model
    model = GadId3Classifier()
    model.fit(x_train, y_train)

    # return accuracy score

    y_pred = model.eval(x_test)
    acc = str(round(accuracy_score(y_test, y_pred) * 100, 3)).replace(".", ",")
    print(f'\nID3 Accuracy: {acc}%')
