from __future__ import print_function
import math
from IPython import display
# from matplotlib import cm
# from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn import metrics
# %tensorflow_version 1.x
import tensorflow as tf
from tensorflow.python.data import Dataset


def preprocess_features(cali_housing_df):
    """Prepares input features from California housing data set.

  Args:
    cali_housing_df: A Pandas DataFrame expected to contain data
      from the California housing data set.
  Returns:
    A DataFrame that contains the features to be used for the model, including
    synthetic features.
  """
    selected_features = cali_housing_df[
        ["latitude",
         "longitude",
         "housing_median_age",
         "total_rooms",
         "total_bedrooms",
         "population",
         "households",
         "median_income"]]
    processed_features = selected_features.copy()
    # Create a synthetic feature.
    processed_features["rooms_per_person"] = (
            cali_housing_df["total_rooms"] /
            cali_housing_df["population"])
    return processed_features


def preprocess_targets(cali_housing_df):
    """Prepares target features (i.e., labels) from California housing data set.

  Args:
    cali_housing_df: A Pandas DataFrame expected to contain data
      from the California housing data set.
  Returns:
    A DataFrame that contains the target feature.
  """
    output_targets = pd.DataFrame()
    # Scale the target to be in units of thousands of dollars.
    output_targets["median_house_value"] = (
            cali_housing_df["median_house_value"] / 1000.0)
    return output_targets


def construct_feature_columns(input_features):
    """Construct the TensorFlow Feature Columns.

  Args:
    input_features: The names of the numerical input features to use.
  Returns:
    A set of feature columns
  """
    return set([tf.feature_column.numeric_column(my_feature) for my_feature in input_features])


def my_input_fn(features, targets, batch_size=1, shuffle=True, num_epochs=None):
    """Trains a linear regression model.

    Args:
      features: pandas DataFrame of features
      targets: pandas DataFrame of targets
      batch_size: Size of batches to be passed to the model
      shuffle: True or False. Whether to shuffle the data.
      num_epochs: Number of epochs for which data should be repeated. None = repeat indefinitely
    Returns:
      Tuple of (features, labels) for next data batch
    """

    # Convert pandas data into a dict of np arrays.
    features = {key: np.array(value) for key, value in dict(features).items()}

    # Construct a dataset, and configure batching/repeating.
    ds = Dataset.from_tensor_slices((features, targets))  # warning: 2GB limit
    ds = ds.batch(batch_size).repeat(num_epochs)

    # Shuffle the data, if specified.
    if shuffle:
        ds = ds.shuffle(10000)

    # Return the next batch of data.
    features, labels = ds.make_one_shot_iterator().get_next()
    return features, labels


def train_model(
        learning_rate,
        steps,
        batch_size,
        training_ex,
        training_tg,
        validation_ex,
        validation_tg):
    """Trains a linear regression model.

    In addition to training, this function also prints training progress information,
    as well as a plot of the training and validation loss over time.

    Args:
      learning_rate: A `float`, the learning rate.
      steps: A non-zero `int`, the total number of training steps. A training step
        consists of a forward and backward pass using a single batch.
      batch_size: A non-zero `int`, the batch size.
      training_ex: A `DataFrame` containing one or more columns from
        `california_housing_dataframe` to use as input features for training.
      training_tg: A `DataFrame` containing exactly one column from
        `california_housing_dataframe` to use as target for training.
      validation_ex: A `DataFrame` containing one or more columns from
        `california_housing_dataframe` to use as input features for validation.
      validation_tg: A `DataFrame` containing exactly one column from
        `california_housing_dataframe` to use as target for validation.

    Returns:
      A `LinearRegressor` object trained on the training data.
    """

    periods = 10
    steps_per_period = steps / periods

    # Create a linear regressor object.
    my_optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate)
    my_optimizer = tf.contrib.estimator.clip_gradients_by_norm(my_optimizer, 5.0)
    linear_regressor = tf.estimator.LinearRegressor(
        feature_columns=construct_feature_columns(training_ex),
        optimizer=my_optimizer
    )

    # Create input functions.
    training_input_fn = lambda: my_input_fn(training_ex,
                                            training_tg["median_house_value"],
                                            batch_size=batch_size)
    predict_training_input_fn = lambda: my_input_fn(training_ex,
                                                    training_tg["median_house_value"],
                                                    num_epochs=1,
                                                    shuffle=False)
    predict_validation_input_fn = lambda: my_input_fn(validation_ex,
                                                      validation_tg["median_house_value"],
                                                      num_epochs=1,
                                                      shuffle=False)

    # Train the model, but do so inside a loop so that we can periodically assess
    # loss metrics.
    print("Training model...")
    print("RMSE (on training data):")
    training_rmse = []
    validation_rmse = []
    for period in range(0, periods):
        # Train the model, starting from the prior state.
        linear_regressor.train(
            input_fn=training_input_fn,
            steps=steps_per_period,
        )
        # Take a break and compute predictions.
        training_predictions = linear_regressor.predict(input_fn=predict_training_input_fn)
        training_predictions = np.array([item['predictions'][0] for item in training_predictions])

        validation_predictions = linear_regressor.predict(input_fn=predict_validation_input_fn)
        validation_predictions = np.array([item['predictions'][0] for item in validation_predictions])

        # Compute training and validation loss.
        training_root_mean_squared_error = math.sqrt(
            metrics.mean_squared_error(training_predictions, training_tg))
        validation_root_mean_squared_error = math.sqrt(
            metrics.mean_squared_error(validation_predictions, validation_tg))
        # Occasionally print the current loss.
        print("  period %02d : %0.2f" % (period, training_root_mean_squared_error))
        # Add the loss metrics from this period to our list.
        training_rmse.append(training_root_mean_squared_error)
        validation_rmse.append(validation_root_mean_squared_error)
    print("Model training finished.")

    # Output a graph of loss metrics over periods.
    plt.ylabel("RMSE")
    plt.xlabel("Periods")
    plt.title("Root Mean Squared Error vs. Periods")
    plt.tight_layout()
    plt.plot(training_rmse, label="training")
    plt.plot(validation_rmse, label="validation")
    plt.legend()

    return linear_regressor


if __name__ == '__main__':
    # tf.logging.set_verbosity(tf.logging.ERROR)
    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
    pd.options.display.max_rows = 10
    pd.options.display.float_format = '{:.1f}'.format

    # california_housing_dataframe = pd.read_csv(
    # "https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
    california_housing_dataframe = pd.read_csv("/Users/bangbui/workspace/AlgorithmInPython/datasets"
                                               "/california_housing_train.csv", sep=",")

    california_housing_dataframe = california_housing_dataframe.reindex(
        np.random.permutation(california_housing_dataframe.index))

    # first row of the dataset
    california_housing_dataframe.describe()

    # Choose the first 12000 (out of 17000) examples for training.
    training_examples = preprocess_features(california_housing_dataframe.head(12000))
    training_targets = preprocess_targets(california_housing_dataframe.head(12000))
    print("training_target:")
    print(training_targets)
    print(california_housing_dataframe["median_house_value"].head().tail() / 1000.0)
    # Choose the last 5000 (out of 17000) examples for validation.
    validation_examples = preprocess_features(california_housing_dataframe.tail(5000))
    validation_targets = preprocess_targets(california_housing_dataframe.tail(5000))

    # Double-check that we've done the right thing.
    print("Training examples summary:")
    display.display(training_examples.describe())
    print("Validation examples summary:")
    display.display(validation_examples.describe())

    print("Training targets summary:")
    display.display(training_targets.describe())
    print("Validation targets summary:")
    display.display(validation_targets.describe())

    # -1.0: perfect negative correlation
    # 0.0: no correlation
    # 1.0: perfect positive correlation
    correlation_dataframe = training_examples.copy()
    correlation_dataframe["target"] = training_targets["median_house_value"]
    # print(correlation_dataframe["target"].head())
    correlation_dataframe.corr()

    #
    # Your code here: add your features of choice as a list of quoted strings.
    #
    minimal_features = [
    ]

    assert minimal_features, "You must select at least one feature!"

    minimal_training_examples = training_examples[minimal_features]
    minimal_validation_examples = validation_examples[minimal_features]

    #
    # Don't forget to adjust these parameters.
    #
    train_model(
        learning_rate=0.001,
        steps=500,
        batch_size=5,
        training_ex=minimal_training_examples,
        training_tg=training_targets,
        validation_ex=minimal_validation_examples,
        validation_tg=validation_targets)
