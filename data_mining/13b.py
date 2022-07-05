import csv
import glob
import itertools
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer

import pandas as pd

pd.options.display.width = 0

stop_word_list = [i[0] for i in csv.reader(open('stop_word.csv', 'r'))]
vectorizer = TfidfVectorizer()


def read_21documents(file_name):
	word_list, tmp = [], []
	with open(file_name, 'r') as f:
		text = f.read()
		tmp.append([i for i in text.split(' ') if 0 < len(i)])
	for word in list(itertools.chain(*tmp)):
		if word not in stop_word_list:
			word_list.append(word)
	result_text = ' '.join(word_list)
	print(f"Text data : {result_text}")
	return result_text


if __name__ == '__main__':
	file_name_list = glob.glob('21Documents/*.txt')
	file_name_list.sort()
	for file_name in file_name_list:
		print('=' * 50)
		print(f' File name = {file_name}')
		print('=' * 50)
		text = read_21documents(file_name)
		text_corpus = text.split('\n')
		print(text_corpus)
		X = vectorizer.fit_transform(text_corpus)
		print(vectorizer.get_feature_names())
		print(X.toarray())
		print('\n')
