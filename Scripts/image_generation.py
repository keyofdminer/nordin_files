from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageFont, ImageDraw

Path("images").mkdir(parents=True, exist_ok=True)


def base():
    b = np.zeros((2560, 1600)[::-1], dtype="uint8") * 255
    return b
    
def square():
    b = np.ones((4, 4)[::-1], dtype="uint8") * 255
    return b


def insert_subimage(img, subimage, x, y):
    img[y : y + subimage.shape[0], x : x + subimage.shape[1]] = subimage


def top_view(*args):
    """
    Stack and display all the supplied images
    """
    fill = 1 / len(args)
    grayscale = np.zeros(args[0].shape, dtype="uint8")
    for i in args:
        grayscale += (i * fill).astype("uint8")
    _, ax = plt.subplots()
    ax.imshow(grayscale[35:85, 35:85], cmap="gray", interpolation=None, vmin=0, vmax=255)
    # ax.imshow(grayscale, cmap="gray", interpolation=None, vmin=0, vmax=255)
    plt.show()

img = base()
square = square()
#for i in range(37):
#    for j in range(22):
#        insert_subimage(img, square, i*71, j*76)
for i in range(5):
    for j in range(5):
        insert_subimage(img, square, i*639, j*399)
top_view(img)
Image.fromarray(img, "L").save("index.png", "PNG")
    
