__doc__ = """
Генератор наборов карточек для игры.
"""

from generators.stable_diffusion_generator import StableDiffusionGenerator
from generators.api_generator import APIGenerator
from generators.mock_generator import MockGenerator
from generators.text_generator import TextGenerator
from generators.words_provider import WordsProvider

from enum import Enum
import subprocess
import random
import shutil
import os

class SetGenerator:
    '''
    Генератор наборов карточек для игры.
    '''
    class Constants(Enum):
        DEFAULT_IMAGE_NAME = 'images/default_image.png' 

    def __init__(self, path, height, width):
        self.path = path
        self.height = height
        self.width = width
        self.generator = StableDiffusionGenerator() # <- Генератор картинок.
        self.generator.configure(height, width)
        self.style = ' in style of Scott Listfield'
        self.text_generator = TextGenerator()
        self.text_generator.configure(WordsProvider())

    def generate_image(self, prompt, path):
        return self.generator.generate_image(prompt, path)

    def generate_set(self, size):
        '''
        Эта функция генерирует картинку по запросу и возвращает путь к папке со сгенерированными картинками,
        после завершения генерации.
        '''
        temp_path = self.path + '/set'
        path = self.path + '/temp_set'
        shutil.rmtree(path + '/samples')
        os.makedirs(path + '/samples')
        for i in range(size):
            prompt = self.text_generator.generate_prompt(self.style)
            self.generate_image(prompt, path)

        os.rename(temp_path, temp_path+'2')
        os.rename(path, temp_path)
        os.rename(temp_path + '2', path)

        return path + '/samples'

    def generate_association(self, prompt):
        '''
        Эта функция генерирует картинку по запросу и возвращает путь к сгенерированной картинке,
        после завершения генерации.

        Если при генерации произошла ошибка, возвращается путь к картинке по умолчанию.
        '''
        directory_path = ''.join(c for c in prompt if  c not in '?:!/;"\' ')
        try:
            os.makedirs(self.path + '/associations/' + directory_path + '/samples')
        except Exception as e:
            print(e)
            
        return self.generate_image(prompt + self.style, self.path + '/associations/' + directory_path)
        
    def clear_folder(self, prompt):
        try:
            directory_path = ''.join(c for c in prompt if  c not in '?:!/;"\' ')
            shutil.rmtree(self.path + '/associations/' + directory_path)
        except Exception as e:
            print(e)
        