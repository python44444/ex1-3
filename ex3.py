from flask import Flask
from flask import render_template
import secrets

from img_2 import make_path, make_img

app = Flask(__name__)

app.secret_key = secrets.token_urlsafe(32)


@app.route("/")
def button():
    return render_template("index.html")


@app.route("/img")
def img():
    im_rgb = make_img()

    out_path = make_path(im_rgb)

    return render_template("color.html", image=out_path)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
