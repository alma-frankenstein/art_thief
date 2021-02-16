from app.pil_image import serve_pil_image
from PIL import Image
from flask import Flask, render_template
from core.surprise_me import get_random_picture
from flask import Response
from flask import send_file
from io import BytesIO

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
    path_to_image, title_artist = get_random_picture()
    img = Image.open(path_to_image)
    return serve_pil_image(img)


@app.route('/sequence')
def generate_images():
    def generate():
        for _ in range(40):
            path_to_image, title_artist = get_random_picture()
            img = Image.open(path_to_image)
            img_io = BytesIO()
            img.save(img_io, 'JPEG', quality=70)
            img_io.seek(0)
            yield send_file(img_io, mimetype='image/jpeg')
    return Response(generate())


# def serve_pil_image(pil_img):
#     img_io = BytesIO()
#     pil_img.save(img_io, 'JPEG', quality=70)
#     img_io.seek(0)
#     return send_file(img_io, mimetype='image/jpeg')

# @app.route('/large.csv')
# def generate_large_csv():
#     def generate():
#         for row in iter_all_rows():
#             yield ','.join(row) + '\n'
#     return Response(generate(), mimetype='text/csv')


# error with /sequence:
# save_pics   : INFO     successfully saved picture.
# Debugging middleware caught exception in streamed response at a point where response headers were already sent.
# Traceback (most recent call last):
#   File "/home/alma/repos/artscrapr/venv/lib/python3.8/site-packages/werkzeug/wsgi.py", line 506, in __next__
#     return self._next()
#   File "/home/alma/repos/artscrapr/venv/lib/python3.8/site-packages/werkzeug/wrappers/base_response.py", line 45, in _iter_encoded
#     for item in iterable:
#   File "/home/alma/repos/artscrapr/src/app/art_thief_app.py", line 40, in generate
#     yield send_file(img_io, mimetype='image/jpeg')
#   File "/home/alma/repos/artscrapr/venv/lib/python3.8/site-packages/flask/helpers.py", line 620, in send_file
#     if current_app.use_x_sendfile and filename:
#   File "/home/alma/repos/artscrapr/venv/lib/python3.8/site-packages/werkzeug/local.py", line 347, in __getattr__
#     return getattr(self._get_current_object(), name)
#   File "/home/alma/repos/artscrapr/venv/lib/python3.8/site-packages/werkzeug/local.py", line 306, in _get_current_object
#     return self.__local()
#   File "/home/alma/repos/artscrapr/venv/lib/python3.8/site-packages/flask/globals.py", line 52, in _find_app
#     raise RuntimeError(_app_ctx_err_msg)
# RuntimeError: Working outside of application context.

# This typically means that you attempted to use functionality that needed
# to interface with the current application object in some way. To solve
# this, set up an application context with app.app_context().  See the
# documentation for more information.
