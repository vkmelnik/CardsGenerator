__doc__ = """
Модуль, предоставляющий слова для генератора текста.
"""

from enum import Enum
import random
import shutil
import os

class WordsProvider:
    '''
    Модуль, предоставляющий слова для генератора текста.
    '''
    class Constants(Enum):
        ADJECTIVES_PATH = 'words/adjectives.txt'
        NOUNS_PATH = 'words/nouns.txt'
        PREPOSITIONS_PATH = 'words/prepositions.txt'
        VERBS_PATH = 'words/verbs.txt'

    def __init__(self):
        with open(self.Constants.ADJECTIVES_PATH.value) as f:
            self.adjectives = [word for line in f for word in line.split()]
        with open(self.Constants.NOUNS_PATH.value) as f:
            self.nouns = [word for line in f for word in line.split()]
        with open(self.Constants.PREPOSITIONS_PATH.value) as f:
            self.prepositions = [word for line in f for word in line.split()]
        with open(self.Constants.VERBS_PATH.value) as f:
            self.verbs = [word for line in f for word in line.split()]
            
    def get_random_noun(self):
        return random.choice(self.nouns)

    def get_random_adjective(self):
        return random.choice(self.adjectives)
        
    def get_random_preposition(self):
        return random.choice(self.prepositions)
        
    def get_random_verb(self):
        return random.choice(self.verbs)
