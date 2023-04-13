Установка:

Скачать модель с https://github.com/CompVis/stable-diffusion и установить в папку CardsGenerator.
Возможно также нужно будет выполнить команду pip install -r requirements.txt

Также нужно скачать веса:
curl https://f004.backblazeb2.com/file/aai-blog-files/sd-v1-4.ckpt > sd-v1-4.ckpt
и создать ссылку, как описано в репозитории с моделью.

Сервис генерации картинок запускается так:
python3 main.py