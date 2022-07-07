"""
M21W0B09 入谷雄介
Data mining 13 class task
"""
import csv
import glob
import itertools
import math
import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn import datasets, preprocessing
from matplotlib import pyplot as plt

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
	def calc_normalized_freq(cls, file_name):
		idf_dict = {}
		text = cls.read_21documents(file_name)
		unique_words = text.split(' ')
		text_corpus = text.split('\n')
		N = len(text_corpus)
		for unique_word in unique_words:
			count = 0
			for sen in text_corpus:
				if unique_word in sen.split():
					count = count + 1
				idf_dict[unique_word] = (math.log((1 + N) / (count + 1))) + 1
		return idf_dict


class CosineSimilarity(IdfUtil):
	@classmethod
	def calc_cosine_similarity(cls, doc_pair):
		docs = [cls.read_21documents(doc_pair[0]), cls.read_21documents(doc_pair[1])]
		vectorizer = TfidfVectorizer(max_df=0.9)
		X = vectorizer.fit_transform(docs)
		print('feature_names:', vectorizer.get_feature_names())
		print('X:')
		print(X.toarray())
		sim = cosine_similarity(X)  # 類似度行列の作成
		for from_id in range(len(docs)):
			print('doc_id:', from_id)
			for to_id in range(len(docs)):
				print('\tsim[{0}][{1}] = {2:f}'.format(
					from_id, to_id, sim[from_id][to_id]))


class Jaccard(IdfUtil):
	@classmethod
	def jaccard(cls, doc1, doc2):
		data1 = cls.read_21documents(doc1).split(' ')
		data2 = cls.read_21documents(doc2).split(' ')
		items = 0
		for item in data1:
			if item in data2:
				items += 1
		print('=' * 50)
		print(doc1, doc2)
		print(items / (len(data1) + len(data2) - items))


class Kmeans(IdfUtil):
	def __init__(self, cluster_num):
		self.docs = self.get_all_documents()
		self.doc_num = len(self.docs)
		self.cluster_num = cluster_num
		self.result_df = pd.DataFrame(columns=['vec'])
		self.convert_vector()

	def separate_kmeans_clusters(self, input_docs):
		for doc_name in input_docs:
			try:
				X = self.result_df.loc[doc_name][0]
				sc = preprocessing.StandardScaler()
				sc.fit(X)
				X_norm = sc.transform(X)
				cls = KMeans(n_clusters=self.cluster_num)
				result = cls.fit(X_norm)
				print(result.labels_)
			except:
				pass

	def convert_vector(self):
		for doc in self.get_all_documents():
			text = self.read_21documents(doc)
			text_corpus = text.split('\n')
			vectorizer.fit_transform(text_corpus)
			X = vectorizer.transform(text_corpus)
			self.result_df.loc[doc] = [X.toarray()]



if __name__ == '__main__':
	# (1)
	WordVector()
	# (2)
	# IDF()
	# (3)
	FreqDamp()

	target_doc1 = ('21Documents/DOC01.txt', '21Documents/DOC02.txt')
	target_doc2 = ('21Documents/DOC01.txt', '21Documents/DOC15.txt')
	target_doc3 = ('21Documents/DOC20.txt', '21Documents/DOC21.txt')

	# (4)
	for target_doc in [target_doc1, target_doc2, target_doc3]:
		CosineSimilarity.calc_cosine_similarity(target_doc1)

	# (5)
	for target_doc in [target_doc1, target_doc2, target_doc3]:
		Jaccard.jaccard(target_doc[0], target_doc[1])

	# (6)
	KmeansObj = Kmeans(3)
	KmeansObj.separate_kmeans_clusters(IdfUtil.get_all_documents())
