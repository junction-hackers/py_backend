from PIL import Image

def crop_image_bounds(path, bound, out_path):
    with Image.open(path) as img:
        cropped_img = img.crop((bound["left"],
                  bound["top"],
                  bound["left"] + bound["width"],
                  bound["top"] + bound["height"]))
        cropped_img.save(out_path)