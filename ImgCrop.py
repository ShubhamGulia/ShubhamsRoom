from PIL import Image
img = Image.open('unsplash.jpg')
area= (768,768,2124,2124)
newimg=img.crop(area)
newimg.show()
