import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from time import time
from sklearn.preprocessing import Normalizer
from sklearn.datasets import make_classification
from sklearn.svm import LinearSVC

from sklearn import svm, datasets

import matplotlib.pyplot as plt


def getData():
    df = pd.read_csv("test_data1_and_name.csv",usecols=['distance','colorSimilarity','result'])
    X = df.values
    return X

def cleanData(X):
    X=np.array([x.astype(float) for x in X if x[0]!='-1' and x[0]!='None' and x[0]!='ERROR' and x[1]!=-1.0 and not np.isnan(x[1])])
    y = X[:,[2]]
    X = np.delete(X, [2], axis=1)
    y=y.flat
    train(X,y)

def train(X,y):
    scaler = Normalizer().fit(X)
    normalizedX = scaler.transform(X)
    clf=LinearSVC()
    model=clf.fit(normalizedX,y)
    # print(model.decision_function([0,0,0]))
    print(model)

    data_test = pd.read_csv("test_data1_and_NOT_MATCH.csv", usecols=['distance', 'colorSimilarity'])
    X = data_test.values
    print(X)
    X = np.array([x.astype(float) for x in X if x[0] != '-1' and x[0] != 'None' and x[0] != 'ERROR' and x[1] != -1.0 and not np.isnan(x[1]) and not np.isnan(x[0])])
    print(X)
    # scaler = Normalizer().fit(X)
    # normalizedX = scaler.transform(X)
    y_test = model.predict(X)
    result = pd.DataFrame(
        {'distance': X[:, 0],
         # 'similarity_result': X[:, 1],
         'colorSimilarity': X[:, 1], 'predict': y_test},
        columns=['distance', 'colorSimilarity', 'predict'])
    result.to_csv("predict_result.csv")


    return model

def predictData(model):
    data_test = pd.read_csv("predict_data.csv", usecols=['distance', 'colorSimilarity'])
    X = data_test.values
    X = np.array([x.astype(float) for x in X if x[0] != '-1' and x[0] != 'None' and x[0] != 'ERROR' and x[1] != -1.0 and not np.isnan(x[1]) and not np.isnan(x[0])])
    print(X)
    # scaler = Normalizer().fit(X)
    # normalizedX = scaler.transform(X)
    y_test = model.decision_function(X)
    result = pd.DataFrame(
        {'distance': X[:, 0],
         # 'similarity_result': X[:, 1],
         'colorSimilarity': X[:, 1], 'predict': y_test},
        columns=['distance', 'similarity_result', 'colorSimilarity', 'predict'])
    result.to_csv("predict_result.csv")

X = getData()
model=cleanData(X)
#predictData(model)


# normalize data
# scaler = Normalizer().fit(X)
# normalizedX = scaler.transform(X)

# def make_meshgrid(x, y, h=.02):
#     """Create a mesh of points to plot in
#
#     Parameters
#     ----------
#     x: data to base x-axis meshgrid on
#     y: data to base y-axis meshgrid on
#     h: stepsize for meshgrid, optional
#
#     Returns
#     -------
#     xx, yy : ndarray
#     """
#     x_min, x_max = x.min() - 1, x.max() + 1
#     y_min, y_max = y.min() - 1, y.max() + 1
#     xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
#                          np.arange(y_min, y_max, h))
#     return xx, yy
#
# def plot_contours(ax, clf, xx, yy, **params):
#     """Plot the decision boundaries for a classifier.
#
#     Parameters
#     ----------
#     ax: matplotlib axes object
#     clf: a classifier
#     xx: meshgrid ndarray
#     yy: meshgrid ndarray
#     params: dictionary of params to pass to contourf, optional
#     """
#     Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
#     Z = Z.reshape(xx.shape)
#     out = ax.contourf(xx, yy, Z, **params)
#     return out
#
# iris = datasets.load_iris()
# print(iris)


# Create dataset of classification task with many redundant and few
# informative features


# Plot calibration curve for Gaussian Naive Bayes





