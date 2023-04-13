__doc__ = """
Генератор картинок, использующий stable-diffusion.
"""

from generators.generator_interface import GeneratorInterface

from enum import Enum
import subprocess
import random
import shutil
import os

class StableDiffusionGenerator(GeneratorInterface):
    class Constants(Enum):
        DEFAULT_IMAGE_NAME = 'images/default_image.png'

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
            subpr = subprocess.Popen(
                f'conda run -n ldm python ./scripts/txt2img.py --prompt \'{prompt}\' --outdir \'../{path}\' --skip_grid --H {self.height} --W {self.width} --plms',
                cwd='./stable-diffusion',
                shell=True, stdout=None,
                stdin=None,
                stderr=None
            )
            subpr.wait()

            sample_path = os.path.join(path, "samples")
            base_count = len(os.listdir(sample_path)) - 1
            filename = os.path.join(sample_path, f"{base_count:05}.png")

            return filename
        except Exception as e:
            print(e)

            return self.Constants.DEFAULT_IMAGE_NAME.value
