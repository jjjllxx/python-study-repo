"""
File: beiyesi.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-02-24 10:15:50
Function:


"""
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

news = fetch_20newsgroups(data_home='all')

x_train, x_test, y_train, y_test = train_test_split(news.data, news.target)

transfer = TfidfVectorizer()
x_train = transfer.fit_transform(x_train)
x_test = transfer.transform(x_test)

estimator = MultinomialNB()
estimator.fit(x_train, y_train)

y_predict = estimator.predict(x_test)
print(y_predict)
print(y_predict == y_test)
score = estimator.score(x_test, y_test)
print(score)
