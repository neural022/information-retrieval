#!/usr/bin/python
# -*- coding: utf-8 -*-

from tokenization import Tokenization

class CorpusPreprocess():
	def __init__(self, version='en'):
		# variable initial
		self.__vocab = dict()
		self.__docs = dict()
		# tokenization
		self.tokenization = Tokenization(version)
	
	def get_file_list(self, file_list_path):
		
		file_list = list()
		with open(file_list_path, 'r', encoding='UTF-8') as f:
			for file_id in f.readlines():
				file_list.append(file_id.strip('\n'))
		
		return file_list
	
	def read_data(self,file_path):
	
		with open(file_path, 'r', encoding='UTF-8') as f:
			text = f.read()
			
		return text
	
	def tokenize(self, text, white_space=True):
	
		if not white_space:
			return self.tokenization.cut(text)
			
		return text.split()
		
	def indexing(self, vocab_list, doc_list):
		# index term
		self.__vocab = { str(vocab_list[i]):i for i in range(len(vocab_list)) }
		self.__docs = { str(doc_list[i]):i for i in range(len(doc_list)) }
		
		return self.__vocab, self.__docs
		