import surprise_me
from pil_image import serve_pil_image
from PIL import Image
from flask import Flask, render_template
from surprise_me import get_random_picture


app = Flask(__name__)


@app.route('/')
@app.route('/surprises')
def surprises():
    return render_template('index.html')


# @app.route('some/route/')
# def serve_img():
#     img = Image.new('RGB', ...)
#     return serve_pil_image(img)

@app.route('/some/route/')
def serve_img():
    # correct AttributeError: 'str' object has no attribute 'save'  ?
    img = Image.open('saved_images/ Abstraction in Red and Green ca 1958 by Henry Botkin.jpg')
    return serve_pil_image(img)


# /home/alma/repos/artscrapr/saved_images / Abstraction in Red and Green ca 1958 by Henry Botkin.jpg
