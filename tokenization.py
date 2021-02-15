#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
import re

# stemming using by PorterStemmer: https://tartarus.org/martin/PorterStemmer/
from stemming import PorterStemmer

class Tokenization():
    
    def __init__(self, version='en'):        
        self.stopwords = set()     
        self.porter_stem = PorterStemmer()
        if version == 'en':
            # shorten patterns  
            self.shorten_patterns = [
                           (r'won\'t', 'will not'),
                           (r'can\'t', 'cannot'),
                           (r'i\'m', 'i am'),
                           (r'(\w+)\'ll', '\g<1> will'),
                           (r'(\w+)n\'t', '\g<1> not'),
                           (r'(\w+)\'ve', '\g<1> have'),
                           (r'(\w+)\'s', '\g<1> is'),
                           (r'(\w+)\'re', '\g<1> are') ]         
            # repeat patterns
            self.repeat_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
            self.repl = r'\1\2\3'
            # remove punctuation pattern, only [a-zA-Z0-9]
            self.punctuation_pattern = re.compile("[^\w]+", re.U)
            # remove number pattern, only [a-zA-Z]
            self.pattern = re.compile("[^\D]+", re.U)
            
        elif version == 'zh-tw':
            self.pattern = ''
            
    def shorten_replace(self, text):
        s = text
        for (pattern, repl) in self.shorten_patterns:
            s = re.sub(pattern, repl, s)
        return s
        
    def remove_punctuation(self, text):
        output_text = ''
        for c in text:
            if c not in string.punctuation:
                output_text += ''.join(c)
            else:
                output_text += ''.join(' ')
        return output_text
    
    def load_stopword_userdict(self, file_name):
        with open(file_name, 'r') as f:
            for word in f.readlines():
                if word not in self.stopwords:
                    self.stopwords.add(word.strip())            
        f.close()
        
    def load_stopword_dict(self):        
        self.load_stopword_userdict('stopwords.txt')
        self.stopwords = list(self.stopwords)
        self.stopwords.sort()
    
    def remove_stopwords(self, text):
        word_sequence = text.split()
        return ' '.join(word for word in word_sequence if word not in self.stopwords) 
                    
    def word_segmentation(self, pattern, word_sequence):
        return ' '.join(word for word in re.sub(pattern, ' ', word_sequence).split())
        
    def stemming(self, text):
        output_text = ''
        for word in text.split():
            output_text += self.porter_stem.stem(word, 0, len(word)-1)
            output_text += ' '
        return output_text
    
    def cut(self, text, shorten=True, punctuation=True, number=True, stopword=True, stemming=True):
        self.text = text.lower()      
        if shorten:
            self.text = self.shorten_replace(self.text)
        if punctuation:
            self.text = self.word_segmentation(self.punctuation_pattern, self.text)
        if number:
            self.text = self.word_segmentation(self.pattern, self.text)      
        if stopword:
            self.load_stopword_dict()
            self.text = self.remove_stopwords(self.text)
        if stemming:
            self.text = self.stemming(self.text)
        word_sequence = self.text.split()
        return ' '.join(word for word in word_sequence)