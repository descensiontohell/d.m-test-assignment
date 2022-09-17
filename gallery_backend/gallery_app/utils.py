import requests


def is_url_image(image_url):
    image_formats = ("image/png", "image/jpeg", "image/jpg")
    r = requests.head(image_url)
    if r.headers.get("content-type") in image_formats:
        return True
    return False
