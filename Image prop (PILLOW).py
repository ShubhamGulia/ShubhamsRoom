from PIL import Image

img = Image.open('unsplash.jpg')
print(img.size)
print(img.format)
img.show()