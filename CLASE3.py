from PIL import Image
from PIL import ImageFilter
filename = "bird.jpg"
with Image.open(filename) as img:
    img.load()

img = img.transpose(Image.FLIP_LEFT_RIGHT)
img = img.filter(ImageFilter.FIND_EDGES)
img.putalpha(70)
img.show()

print(img.format)
print(img.size)
print(img.mode)

img.save("putalfa.jpg")