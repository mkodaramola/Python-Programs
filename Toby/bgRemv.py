from rembg import remove
from PIL import Image


iPath = 'c.jpg'
oPath = 'p.png'

input = Image.open(iPath)
output = remove(input)
output.save(oPath)