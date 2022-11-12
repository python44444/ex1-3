from flask import Flask
from flask import render_template
import secrets
import numpy as np
from PIL import Image

from img import make_path

app = Flask(__name__)

app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def button():
    return render_template("index.html")


def make_img():
    row_data = []
    h = np.random.randint(0, 255)
    for v in range(256):
        row_data.append(h)

    hue_data = np.tile(row_data, (256, 1))
    sat_data = np.transpose(hue_data)
    val_data = np.full_like(hue_data, 255)
    mat_data = np.stack([hue_data, sat_data, val_data], 2)

    im = Image.fromarray(np.uint8(mat_data), "HSV")
    im_data = im.convert("RGB")

    return im_data


@app.route("/img")
def img():
    im_rgb = make_img()

    out_path = make_path(im_rgb)

    return render_template("color.html", image=out_path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
