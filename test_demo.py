#coding:utf-8
'''

Created on 2017.6.11
@author: jjwang

'''
from gensim import models
import logging

def test():
	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
	model = models.KeyedVectors.load_word2vec_format('word.emb', binary = True)

	print("providing 2 different testing scenarios\n")
	print("input: one word; output: top 100 most similar words")
	print("input: two words; output: cosine value")
	while 1:
		try:
			text = raw_input()
			word_list = text.split()

			if len(word_list) == 1:
				print("finding top 100 most similar words。。。")
				items = model.most_similar(word_list[0],topn = 100)
				for item in items:
					print(item[0]+","+str(item[1]))

			elif len(word_list) == 2:
				print("computing cosine value。。。")
				cosine_value = model.similarity(word_list[0],word_list[1])
				print(cosine_value)

			print("===============next=================")
		except Exception as e:
			print(repr(e))

if __name__ == "__main__":
	test()
