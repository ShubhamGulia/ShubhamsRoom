from PIL import Image
img1= Image.open('#image1')#(size assume 400,400)
img2= Image.open('#image1')#(size assume 100,100)

# if area specified is not exact it will trow error
area=(100,100,300,300)
img1.paste(img2,area)