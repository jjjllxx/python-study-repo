"""
File: yuanweihua.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-02-05 15:01:25
Function:


"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV


def knn_iris_gscv():
    iris = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=6)

    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)

    estimator = KNeighborsClassifier(n_neighbors=3)
    param_dict = {'n_neighbors': [1, 3, 5, 7, 9]}
    estimator = GridSearchCV(estimator, param_grid=param_dict, cv=10)
    estimator.fit(x_train, y_train)

    y_predict = estimator.predict(x_test)
    print(y_predict)
    print(y_predict == y_test)
    score = estimator.score(x_test, y_test)
    print(score)
    print(estimator.best_params_)
    print(estimator.best_score_)


def knn_iris():
    iris = load_iris()
    x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=6)

    transfer = StandardScaler()
    x_train = transfer.fit_transform(x_train)
    x_test = transfer.fit_transform(x_test)

    estimator = KNeighborsClassifier()
    estimator.fit(x_train, y_train)

    y_predict = estimator.predict(x_test)
    print(y_predict)
    print(y_predict == y_test)
    score = estimator.score(x_test, y_test)
    print(score)


knn_iris_gscv()
