__doc__ = """
Генератор текста для генерации наборов карточек для игры.
"""

from enum import Enum
import random
import shutil
import os

class WordTypes(Enum):
    noun = 1
    verb = 2
    adjective = 3
    preposition = 4

class TextGenerator:
    '''
    Генератор текста для генерации наборов карточек для игры.
    '''

    def __init__(self):
        self.order = [
            WordTypes.noun,
            WordTypes.verb,
            WordTypes.adjective,
            WordTypes.noun,
            WordTypes.preposition,
            WordTypes.adjective,
            WordTypes.noun
        ]
            
    def configure(self, words_provider):
        self.words_provider = words_provider

    def get_word(self, case):
        if case == WordTypes.noun:
            return self.words_provider.get_random_noun()
        elif case == WordTypes.verb:
            return self.words_provider.get_random_verb()
        elif case == WordTypes.adjective:
            return self.words_provider.get_random_adjective()
        else:
            return self.words_provider.get_random_preposition()

    def generate_prompt(self, style):
        prompt = ' '.join([self.get_word(case) for case in self.order])

        prompt += style
        print(prompt)

        return prompt
