import csv
import glob
import itertools
from sklearn.feature_extraction.text import TfidfVectorizer

stop_word_list = [i[0] for i in csv.reader(open('stop_word.csv', 'r'))]
vectorizer = TfidfVectorizer()


class WordVector:
	def __init__(self):
		self.generate_word_vector()

	@classmethod
	def read_all_documents(cls):
		file_name_list = glob.glob('21Documents/*.txt')
		file_name_list.sort()
		return file_name_list

	@classmethod
	def read_21documents(cls, file_name):
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

	@classmethod
	def generate_word_vector(cls):
		for file_name in cls.read_all_documents():
			print('=' * 50)
			print(f' File name = {file_name}')
			print('=' * 50)
			text = cls.read_21documents(file_name)
			text_corpus = text.split('\n')
			print(text_corpus)
			X = vectorizer.fit_transform(text_corpus)
			print(vectorizer.get_feature_names())
			print(X.toarray())
			print('\n')


if __name__ == '__main__':
	WordVector()
