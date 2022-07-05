"""
M21W0B09 入谷雄介
Data mining 13 class task
"""

import csv
import glob
import itertools

from sklearn.feature_extraction.text import TfidfVectorizer

stop_word_list = [i[0] for i in csv.reader(open('stop_word.csv', 'r'))]
vectorizer = TfidfVectorizer()


class IdfUtil:
	@staticmethod
	def get_all_documents():
		file_name_list = glob.glob('21Documents/*.txt')
		file_name_list.sort()
		return file_name_list

	@staticmethod
	def read_21documents(file_name) -> str:
		word_list, tmp = [], []
		with open(file_name, 'r') as f:
			text = f.read()
			tmp.append([i for i in text.split(' ') if 0 < len(i)])
		for word in list(itertools.chain(*tmp)):
			if word not in stop_word_list:
				word_list.append(word)
		result_text = ' '.join(word_list)
		return result_text


class WordVector(IdfUtil):
	def __init__(self):
		self.generate_word_vector()

	@classmethod
	def generate_word_vector(cls):
		for file_name in cls.get_all_documents():
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


class IDF(IdfUtil):
	def __init__(self):
		self.calc_idf()

	@classmethod
	def calc_idf(cls):
		idf_dict = {}
		document_list = cls.get_all_documents()
		for file_name in document_list:
			text = cls.read_21documents(file_name)
			text_corpus = text.split('\n')
			vectorizer.fit_transform(text_corpus)
			for word in vectorizer.get_feature_names():
				if word not in idf_dict:
					idf_dict[word] = 0
				idf_dict[word] += 1
		for key, value in idf_dict.items():
			idf_dict[key] = round(len(document_list) / value, 2)
		print('=' * 30, 'Inverse Document Frequency', '=' * 30)
		print(idf_dict)


class FreqDamp(IdfUtil):
	def __init__(self):
		self.calc_freq_damp()

	@classmethod
	def calc_freq_damp(cls):
		freq_damp_dict = {}
		document_list = cls.get_all_documents()
		for file_name in document_list:
			text = cls.read_21documents(file_name)
			text_corpus = text.split('\n')
			vectorizer.fit_transform(text_corpus)
			for word in vectorizer.get_feature_names():
				if word not in freq_damp_dict:
					freq_damp_dict[word] = 0
				freq_damp_dict[word] += 1
		for key, value in freq_damp_dict.items():
			freq_damp_dict[key] = round(value / len(document_list), 2)
		print('=' * 30, 'Frequency Damping', '=' * 30)
		print(freq_damp_dict)


class NormalizedFreq(IdfUtil):
	@classmethod
	def calc_normalized_freq(cls):
		normalized_freq_dict = {}
		document_list = cls.get_all_documents()
		for file_name in document_list:
			text = cls.read_21documents(file_name)
			text_corpus = text.split('\n')
			vectorizer.fit_transform(text_corpus)
			for word in vectorizer.get_feature_names():
				if word not in normalized_freq_dict:
					normalized_freq_dict[word] = 0
				normalized_freq_dict[word] += 1
		for key, value in normalized_freq_dict.items():
			normalized_freq_dict[key] = round(value / len(document_list), 2)
		print('=' * 30, 'Normalized Frequency', '=' * 30)
		print(normalized_freq_dict)


class CosineSimilarity(IdfUtil):
	@classmethod
	def calc_cosine_similarity(cls):
		document_list = cls.get_all_documents()
		for file_name in document_list:
			text = cls.read_21documents(file_name)
			text_corpus = text.split('\n')
			vectorizer.fit_transform(text_corpus)
			X = vectorizer.transform(text_corpus)
			print(X.toarray())
			print('\n')


if __name__ == '__main__':
	# WordVector()
	# IDF()
	FreqDamp()
	print(NormalizedFreq())
	CosineSimilarity.calc_cosine_similarity()

