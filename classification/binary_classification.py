

import numpy as np
import pandas as pd
import tensorflow as tf
from matplotlib import pyplot as plt


def init_config():
    # The following lines adjust the granularity of reporting.
    pd.options.display.max_rows = 10
    pd.options.display.float_format = "{:.1f}".format
    # tf.keras.backend.set_floatx('float32')

    print("Ran the import statements.")


def load_dataset():
    train_df = pd.read_csv("~/workspace/AlgorithmInPython/datasets/california_housing_train.csv")
    test_df = pd.read_csv("~/workspace/AlgorithmInPython/datasets/california_housing_test.csv")
    train_df = train_df.reindex(np.random.permutation(train_df.index))  # shuffle the training set


if __name__ == '__main__':
    init_config()
    load_dataset()


