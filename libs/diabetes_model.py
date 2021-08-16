import os
import numpy as np
from sklearn import datasets, linear_model
from joblib import dump

# model_saving_path = f"{os.getcwd()}/storage/diabetes.model"
# print(model_saving_path)


def train_diabetes_model():
    diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

    diabetes_X = diabetes_X[:, np.newaxis, 2]

    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]

    diabetes_y_train = diabetes_y[:-20]
    diabetes_y_test = diabetes_y[-20:]

    regr = linear_model.LinearRegression()

    regr.fit(diabetes_X_train, diabetes_y_train)

    model_saving_path = f"{os.getcwd()}/storage/diabetes.model"

    print(model_saving_path)
    dump(regr, model_saving_path)


if __name__ == "__main__":
    train_diabetes_model()
