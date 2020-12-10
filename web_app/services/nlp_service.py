# Use gensim model functions for NLP
 
from gensim import corpora, models, similarities
from collections import defaultdict
from pprint import pprint

from nltk.tokenize import TweetTokenizer

class DocCompair():
    
    def __init__(self, texts):
        """input: texts is a list of strings"""
        self.texts = texts        
        self.stoplist = set('for a of the and to in at on by . , '.split(' '))

    def tokenize(self):
        """tokenize texts"""
        texts = self.texts
        
        self.tokenizer = TweetTokenizer()
        sentences = [self.tokenizer.tokenize(text) for text in texts]
        # pprint(sentences)
        
        # genrate tokenized texts as dictionary
        self.tokenized_texts = [[t for t in sentence if t not in self.stoplist] for sentence in sentences]
        # pprint(self.tokenized_texts)        

    def build_dictionary(self):
        """generate dictionary from texts, keeping word appeared equal or more than least_frequency"""              
        
        self.dictionary = corpora.Dictionary(self.tokenized_texts)
        self.vec_dict = [self.dictionary.doc2bow(s) for s in self.tokenized_texts]

    
    def similarity(self, new_str):
        """ return the similarity of the input string to the dictionary"""
        # train the model
        tfidf = models.TfidfModel(self.vec_dict)
        
        # generate a vector for the new string
        sentence = self.tokenizer.tokenize(new_str)
        
        tokens = [s for s in sentence if s not in self.stoplist]

        new_vec = self.dictionary.doc2bow(tokens)
        
        # 
        index = similarities.SparseMatrixSimilarity(tfidf[self.vec_dict], num_features=len(self.dictionary))

        sims = index[tfidf[new_vec]]
        #pprint(list(enumerate(sims)))
        # return the similarities of the new_str to the text corpus
        return sims


if __name__ == "__main__":

    texts = ['This is a good students test','Teachers control test GPA below 4.0','A very good day for test students and teachers.']

    dc = DocCompair(texts)
    dc.tokenize()
    pprint(dc.tokenized_texts)
    dc.build_dictionary()
    pprint(dc.dictionary.token2id)
    pprint(dc.vec_dict)

    new = 'Students do not come in on sunday, not a test day.'
    sims = dc.similarity(new)
    
