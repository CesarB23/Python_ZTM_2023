from PIL import Image,ImageFilter

img = Image.open('./Images/jpeg-home.jpg')
# filter_img = img.filter(ImageFilter.BLUR)
filter_img = img.convert('L')
# filter_img.save("grey.png","png")
crooked = filter_img.rotate(90)
filter_img.show()
# crooked.save("rotated.png","png")
resize = filter_img.resize((300,300))
resize.show()