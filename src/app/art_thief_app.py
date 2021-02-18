from random import randint

from flask import Flask, render_template
from flask import url_for

from src.app.pil_image import serve_pil_image
from src.core.get_and_save_pic import get_artist_title_from_artsy_url, get_image_from_artsy
from src.core.surprise_me import filter_collections, get_random_picture, rand_collection_href, random_picture_in_collection

app = Flask(__name__)


@app.route('/random')
def some_image():
    return render_template('image_framed.html', img_url=url_for('serve_img', seed=randint(0, 1_000_000_000)))


@app.route('/randomimg_<seed>.jpg')
def serve_img(seed):
    img, title_artist = get_random_picture()
    return serve_pil_image(img)


@app.route('/randomimg_<path:img_path>')
def serve_saved_img(img_path):
    img = get_image_from_artsy(img_path)
    return serve_pil_image(img)


@app.route('/')
@app.route('/random_with_info')
def some_image_with_more_info():
    filtered_collections = filter_collections()
    collection_href = rand_collection_href(filtered_collections)
    some_url = random_picture_in_collection(collection_href)
    title_artist = get_artist_title_from_artsy_url(some_url)

    return render_template('image_framed.html',
                           img_url=url_for('serve_saved_img',
                                           img_path=some_url),
                           artist_info=title_artist)
