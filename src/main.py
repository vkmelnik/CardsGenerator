from flask import Flask, send_file, request, abort, make_response, jsonify
import subprocess
import base64
import os

from set_generator import SetGenerator

app = Flask(__name__)

@app.route('/')
def index():
    return 'Привет мир!'

@app.route('/picture')
def get_image():
    association = request.args.get('association')
    set_generator = SetGenerator('images', 512, 512)
    
    response = None

    filename = set_generator.generate_association(association)
    with open(filename, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        response = make_response(jsonify(encoded_image), 200)
        
    set_generator.clear_folder(association)
    
    return abort(500) if (response is None) else response

@app.route('/new_pictures')
def generate_new_set():
    n = request.args.get('n')
    set_size = int(n)

    set_generator = SetGenerator('images', 512, 512)

    set_generator.generate_set(set_size)

    return 'Ok'

@app.route('/pictures')
def get_images():
    n = request.args.get('n')
    set_size = int(n)

    images = []
    path = "images/set/samples"
    for filename in os.listdir(path):
        if filename.endswith(".png"):
            with open(os.path.join(path, filename), "rb") as image_file:
                if len(images) < set_size:
                    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
                    images.append(encoded_image)
                    print(f'Converted {len(images)} images to base64.')

    return make_response(jsonify(images), 200)

@app.route('/settings')
def set_settings():
    return 'Ok'

if __name__ == "__main__":
    app.run(host='0.0.0.0')