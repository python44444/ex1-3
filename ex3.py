from flask import Flask
from PIL import Image
from flask import render_template

# import requests
import numpy as np

app = Flask(__name__)


@app.route("/")
def button():
    return render_template("index.html")


@app.route("/img")
def img():
    row_data = []
    h = np.random.randint(0, 255)
    for v in range(256):
        row_data.append(h)
    # return row_data

    hue_data = np.tile(row_data, (256, 1))
    sat_data = np.transpose(hue_data)
    val_data = np.full_like(hue_data, 255)
    # val_data = np.full_like(hue_data, 384)
    mat_data = np.stack([hue_data, sat_data, val_data], 2)

    im = Image.fromarray(np.uint8(mat_data), "HSV")
    im_rgb = im.convert("RGB")

    im_resize = im_rgb.resize((384, 256))
    im_resize.save("static/images/out.png")
    path = "static/images/out.png"

    return render_template("color.html", image=path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
