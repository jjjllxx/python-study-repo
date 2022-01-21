"""
File: shujuji.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-02-01 15:27:34
Function:


"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)
print(x_train)
print(iris['DESCR'])
