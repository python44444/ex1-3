# from flask import Flask
# from PIL import Image
# from flask import render_template
# import numpy as np

# from img import make

# app = Flask(__name__)


# @app.route("/")
# def button():
#     return render_template("index.html")


# @app.route("/img")
# def img():
#     row_data = []
#     h = np.random.randint(0, 255)
#     for v in range(256):
#         row_data.append(h)

#     hue_data = np.tile(row_data, (256, 1))
#     sat_data = np.transpose(hue_data)
#     val_data = np.full_like(hue_data, 255)
#     mat_data = np.stack([hue_data, sat_data, val_data], 2)

#     im = Image.fromarray(np.uint8(mat_data), "HSV")
#     im_rgb = im.convert("RGB")

#     im_resize = im_rgb.resize((384, 256))
#     im_resize.save("static/images/out.png")
#     path = "static/images/out.png"

#     return render_template("color.html", image=path)


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", debug=True, port=5000)


from flask import Flask
from PIL import Image
from flask import render_template
import numpy as np
import secrets

from img import make

app = Flask(__name__)

app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def button():
    return render_template("index.html")


@app.route("/img")
def img():
    row_data = []
    h = np.random.randint(0, 255)
    for v in range(256):
        row_data.append(h)

    hue_data = np.tile(row_data, (256, 1))
    sat_data = np.transpose(hue_data)
    val_data = np.full_like(hue_data, 255)
    mat_data = np.stack([hue_data, sat_data, val_data], 2)

    im = Image.fromarray(np.uint8(mat_data), "HSV")
    im_rgb = im.convert("RGB")

    outpath = make(im_rgb)

    return render_template("color.html", image=outpath)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
