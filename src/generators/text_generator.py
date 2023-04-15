__doc__ = """
Генератор текста для генерации наборов карточек для игры.
"""

from enum import Enum
import random
import shutil
import os

class TextGenerator:
    '''
    Генератор текста для генерации наборов карточек для игры.
    '''

    def __init__(self):
        pass
            
    def configure(self, words_provider):
        self.words_provider = words_provider

    def generate_prompt(self, style):
        prompt = self.words_provider.get_random_adjective()
        prompt += ' ' + self.words_provider.get_random_noun()
        prompt += ' ' + self.words_provider.get_random_verb()
        prompt += ' ' + self.words_provider.get_random_adjective()
        prompt += ' ' + self.words_provider.get_random_noun()
        prompt += ' ' + self.words_provider.get_random_preposition()
        prompt += ' ' + self.words_provider.get_random_adjective()
        prompt += ' ' + self.words_provider.get_random_noun()

        prompt += style

        return prompt
