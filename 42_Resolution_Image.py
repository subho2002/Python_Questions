from PIL import Image

img = PIL.Image.open("/Path")

width,height = img.size

print(width,"X",height)