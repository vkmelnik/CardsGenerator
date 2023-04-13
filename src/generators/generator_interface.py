__doc__ = """
Интерфейс генератора картинок.
"""

class GeneratorInterface:
    def __init__(self):
        pass
    def configure(self, height, width):
        pass
    def generate_image(self, prompt, path):
        pass