import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import config
from algorithms.id3.ID3 import GadId3Classifier
from utils.landing_club_util import get_columns


# TODO: get data from read_data()
# TODO: use check_accuracy from util_tree
def run_id3():
    df = pd.read_csv(config.dataset_path, header=1)

    # rename known columns
    df.columns = get_columns()

    # organize data into input and outputs
    x = df.drop(columns="status")
    y = df["status"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33)

    # initialize and fit model
    model = GadId3Classifier()
    model.fit(x_train, y_train)

    # return accuracy score
    y_pred = model.predict(x_test)
    print(f'ID3 Accuracy: {accuracy_score(y_test, y_pred) * 100:.3f}%')


