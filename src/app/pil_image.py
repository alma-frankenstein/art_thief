""" Take a PIL image and send to server """

from io import BytesIO

from PIL.Image import Image
from flask import send_file


def serve_pil_image(pil_img: Image):
    """Send image file to server"""
    img_io = BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')
