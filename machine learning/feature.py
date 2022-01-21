"""
File: tezheng.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2021-02-01 16:25:43
Function:


"""
# from sklearn.feature_extraction import DictVectorizer
# from sklearn.feature_extraction.text import CountVectorizer

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer

data1 = [{'city': '北京', 'temperature': 100}, {'city': '上海', 'temperature': 60}, {'city': '深圳', 'temperature': 30}]
data2 = ['life is is short, i like python', 'life is too long, i dislike python']

transfer2 = CountVectorizer(stop_words=['is', 'too'])
transfer1 = DictVectorizer(sparse=False)
data1_new = transfer1.fit_transform(data1)
data2_new = transfer2.fit_transform(data2).toarray()


print(data2_new, transfer2.get_feature_names())
