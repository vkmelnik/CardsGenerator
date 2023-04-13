__doc__ = """
Генератор картинок, использующий api сайта https://api.deepai.org/api/text2img.
"""

from generators.generator_interface import GeneratorInterface

from PIL import Image
from enum import Enum
import requests
import random
import shutil
import os

class APIGenerator(GeneratorInterface):
    class Constants(Enum):
        DEFAULT_IMAGE_NAME = './images/default_image.png'
        URL = "https://api.deepai.org/api/text2img"
        API_KEY = 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'

    def __init__(self):
        pass

    def configure(self, height, width):
        self.height = height
        self.width = width

    def generate_image(self, prompt, path):
        '''
        Эта функция генерирует картинку по запросу и возвращает путь к сгенерированной картинке,
        после завершения генерации.

        Если при генерации произошла ошибка, возвращается путь к картинке по умолчанию.
        '''
        print('Generating image for ', prompt)
        try:
            r = requests.post(
                self.Constants.URL.value,
                data={
                    'text': prompt,
                },
                headers={'api-key': self.Constants.API_KEY.value}
            )
            if r.status_code != 200:
                raise Exception(f'API responded with {r.status_code}')

            output_url = r.json().output_url

            sample_path = os.path.join(path, "samples")
            base_count = len(os.listdir(sample_path))
            download_filename = os.path.join(sample_path, f"{base_count:05}.jpg")
            filename = os.path.join(sample_path, f"{base_count:05}.png")

            response = requests.get(output_url)
            if response.status_code == 200:
                with open(download_filename, 'wb') as f:
                    f.write(response.content)

            im = Image.open(download_filename)
            im.save(filename, "PNG")
            os.remove(download_filename)

            return filename
        except Exception as e:
            print(e)

            return self.Constants.DEFAULT_IMAGE_NAME.value
