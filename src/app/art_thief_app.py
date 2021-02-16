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
    # get_random_picture()
    img = Image.open('src/static/temp_image.jpg')
    return serve_pil_image(img)
