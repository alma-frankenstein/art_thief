from app.pil_image import serve_pil_image
from PIL import Image
from flask import Flask, render_template
from core.surprise_me import get_random_picture

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
    path_to_image = get_random_picture()
    img = Image.open('src/static/temp_image.jpg')
    # img = Image.open(path_to_image)    # current:   home/alma/repos/artscrapr/src/saved_images/Handmade Noise 2017 by Vik Muniz.jpg
    return serve_pil_image(img)
