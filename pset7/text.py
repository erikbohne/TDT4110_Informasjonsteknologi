"""
Module for task 2 in Moduler.ipynb

A class that represents a text and can be used to perform various operations on it.
"""

class Text:
    
    def __init__(self, text):
        
        if type(text) == str:
            self.text = text
        else:
            raise TypeError("Text must be a string!")
        
    def count_words(self):
        return len(self.text.split())
    
    def count_chars(self):
        return len(self.text)
    
    def longest_word(self):
        return max(self.text.split(), key=len)
    
    def longest_sentence(self):
        return max(self.text.split("."), key=len)
    
    def reverse(self):
        return self.text[::-1]
        
    def __str__(self):
        return self.text
    
    def __repr__(self):
        return self.text
    
    def __iter__(self):
        return iter(self.text)
    
    def __next__(self):
        return next(self.text)
    
    def __len__(self):
        return len(self.text)
    
    def __add__(self, other):
        return Text(self.text + other.text)

        
    