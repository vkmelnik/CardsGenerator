__doc__ = """
Заглушка для тестирования.
"""

from generators.generator_interface import GeneratorInterface

from PIL import Image
from enum import Enum
import requests
import random
import shutil
import os

class MockGenerator(GeneratorInterface):
    class Constants(Enum):
        DEFAULT_IMAGE_NAME = 'images/default_image.png'
        MOCK_IMAGES_PATH = 'mock_images'

    def __init__(self):
        pass

    def configure(self, height, width):
        self.height = height
        self.width = width

    def generate_image(self, prompt, path):
        '''
        Если при генерации произошла ошибка, возвращается путь к картинке по умолчанию.
        '''
        print('Generating image for ', prompt)
        try:
            sample_path = os.path.join(path, "samples")
            base_count = len(os.listdir(sample_path))
            filename = os.path.join(sample_path, f"{base_count:05}.png")

            mock_path = self.Constants.MOCK_IMAGES_PATH.value
            mock_count = random.randint(0, len(os.listdir(mock_path)) - 2)
            mock_filename = os.path.join(mock_path, f"{mock_count:05}.png")

            self.resize(mock_filename, filename)

            return filename
        except Exception as e:
            print(e)

            return self.Constants.DEFAULT_IMAGE_NAME.value

    def resize(self, from_path, to_path):
        size = self.width, self.height
        image = Image.open(from_path)
        image = image.resize(size, Image.LANCZOS)
        image.save(to_path, "PNG")
