Установка:

Скачать модель с https://github.com/CompVis/stable-diffusion и установить в папку src.
При генерации, многие изображения могут быть ошибочно подвергнуты цензуре.
При необходимости отключения цензуры, нужно в файле src/stable-diffusion/scripts/txt2img.py
заменить содержимое функции def check_safety(x_image): на return x_image, False


Необходимо выполнить команду pip install -r requirements.txt для установки необходимых библиотек.

Также нужно скачать веса:
curl https://f004.backblazeb2.com/file/aai-blog-files/sd-v1-4.ckpt > sd-v1-4.ckpt
и создать ссылку, как описано в репозитории с моделью.

Сервис генерации картинок запускается из папки src так:
python3 main.py
