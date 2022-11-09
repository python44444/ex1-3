def make(color):
    output_path = "static/images/out.png"
    im_resize = color.resize((384, 256))
    im_resize.save(output_path)
    return output_path
