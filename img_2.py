import numpy as np
from PIL import Image


def make_path(color_img):
    output_path = "static/images/out.png"
    im_resize = color_img.resize((384, 256))
    im_resize.save(output_path)
    return output_path


def make_img():
    h = np.random.randint(0, 255)
    i = np.random.randint(0, 255)
    j = np.random.randint(0, 255)
    k = np.random.randint(0, 255)
    im_data = Image.new("RGBA", (384, 256), (h, i, j, k))

    return im_data
