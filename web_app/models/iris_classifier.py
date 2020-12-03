# web_app/iris_classifier.py

import os
import pickle

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression  # for example

SAVE_MODEL = os.path.join(os.path.dirname(
    __file__), "trained_classifier_iris.pkl")

# print(MODEL_FILEPATH)  #> web_app/models/../models/latest_model.pkl

def train_and_save_model():
    print("TRAINING THE MODEL...")
    X, y = load_iris(return_X_y=True)
    #print(type(X), X.shape) #> <class 'numpy.ndarray'> (150, 4)
    #print(type(y), y.shape) #> <class 'numpy.ndarray'> (150,)
    classifier = LogisticRegression()  # for example
    classifier.fit(X, y)

    print("SAVING THE MODEL...")
    with open(SAVE_MODEL, "wb") as f:
        pickle.dump(classifier, f)

    return classifier


def load_model():
    print("LOADING THE MODEL...")
    with open(SAVE_MODEL, "rb") as f:
        trained_model = pickle.load(f)
    return trained_model


if __name__ == "__main__":

    train_and_save_model()

    clf = load_model()
    print("CLASSIFIER:", clf)

    # check if classifier can predict
    X, y = load_iris(return_X_y=True)

    inputs = X[:2, :]
    print(type(inputs), inputs)

    result = clf.predict(inputs)
    print("RESULT:", result)
