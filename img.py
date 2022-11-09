import numpy as np
from PIL import Image


def make_path(color_img):
    output_path = "static/images/out.png"
    im_resize = color_img.resize((384, 256))
    im_resize.save(output_path)
    return output_path


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
    im_rgb = im.convert("RGB")

    return im_rgb
