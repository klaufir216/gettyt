import sys
import argparse
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image
import requests

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"


def get_urls(id):
    url1 = f'https://media.gettyimages.com/photos/-id{id}?s=2048x2048&w=5'
    url2 = f'https://media.gettyimages.com/photos/-id{id}?s=2048x2048&w=125'
    return url1, url2


def get_image(url):
    headers = { 'User-Agent': USER_AGENT }
    return requests.get(url, headers=headers)


def merge_images(img1, img2):
    w, h = img1.width, img1.height
    split_height = int(h/5*3)
    rect1 = (0, 0, w, split_height)
    rect2 = (0, split_height, w, h)
    img1_cropped = img1.crop(rect1)
    img2_cropped = img2.crop(rect2)
    new_image = Image.new("RGB", (w, h))
    new_image.paste(img1_cropped)
    new_image.paste(img2_cropped, (0, split_height))
    return new_image


def getty_download(getty_id):
    url1, url2 = get_urls(getty_id)
    response1 = get_image(url1)
    response2 = get_image(url2)

    img1 = Image.open(BytesIO(response1.content))
    img2 = Image.open(BytesIO(response2.content))
    new_image = merge_images(img1, img2)
    # getty saves jpeg with q=85
    # here q=86 is used to counteract reencode quality loss
    new_image.save(f'{getty_id}.jpg', quality=86, exif=img1.info['exif'])

def get_id_from_url(url):
    return urlparse(url).path.split('/')[-1]

def main(args):
    parser = argparse.ArgumentParser(
        prog = 'gettyt',
        description = 'getty image downloader')
    parser.add_argument('id_or_url')
    args = parser.parse_args(args)
    if args.id_or_url.startswith('https'):
        getty_id = get_id_from_url(args.id_or_url)
    else:
        getty_id = args.id_or_url
    return getty_download(getty_id)
