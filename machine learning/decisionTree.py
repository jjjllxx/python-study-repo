"""
File: jueceshu.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-02-25 12:11:27
Function:


"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22)

estimator = DecisionTreeClassifier(criterion='entropy')
estimator.fit(x_train, y_train)
y_predict = estimator.predict(x_test)
print(y_predict)
print(y_predict == y_test)
score = estimator.score(x_test, y_test)
print(score)