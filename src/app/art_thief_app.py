from random import randint

from flask import Flask, render_template
from flask import url_for

from src.app.pil_image import serve_pil_image
from src.core.surprise_me import get_random_picture

app = Flask(__name__)


@app.route('/')
@app.route('/surprises')
def surprises():
    return render_template('index.html')


@app.route('/random')
def some_image():
    return render_template('image_framed.html', img_url=url_for('serve_img', seed=randint(0, 1_000_000_000)))


@app.route('/randomimg_<seed>.jpg')
def serve_img(seed):
    img, title_artist = get_random_picture()
    return serve_pil_image(img)
