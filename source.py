# static_analysis_example/source.py

import os

def get_image(url):
    command = "wget -q https:{}".format(url)
    return os.system(command)

def convert():
    image_link = input("image link: ")
    image = get_image(image_link)