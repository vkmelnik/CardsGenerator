__doc__ = """
Генератор наборов карточек для игры.
"""

from generators.stable_diffusion_generator import StableDiffusionGenerator
from generators.api_generator import APIGenerator
from generators.mock_generator import MockGenerator

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
        self.generator = MockGenerator() # <- Генератор картинок.
        self.generator.configure(height, width)
        with open('texts/TheAdventureoftheDancingMen-ArthurConanDoyle') as f:
            self.words = [ word for line in f for word in line.split() ]

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
            max_index = len(self.words) - 1
            start = random.randint(0, max(1, max_index))
            end = min(start + random.randint(2, 5), max_index)
            prompt = ' '.join(self.words[start:end])
            prompt = ''.join( c for c in prompt if  c not in '?:!/;"\'' )
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
            
        return self.generate_image(prompt, self.path + '/associations/' + directory_path)
        
    def clear_folder(self, prompt):
        try:
            directory_path = ''.join(c for c in prompt if  c not in '?:!/;"\' ')
            shutil.rmtree(self.path + '/associations/' + directory_path)
        except Exception as e:
            print(e)
        