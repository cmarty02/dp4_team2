# modulo.py
from fastai.vision.all import PILImage

def get_x(x):
    return PILImage.create(x['image'])

def get_y(x):
    return x['label']
