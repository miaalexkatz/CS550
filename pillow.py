from PIL import Image

imgx = 512
imgy = 512
sat = 255
image = Image.new("RGB", (imgx, imgy))
for x in range(imgx):
	for y in range(imgy):
		sat -= 1
		if sat == 0:
			sat = 255
		image.putpixel((x,y),(x,y,sat))

def pixel(x, y):
	for a in range(15):
		for b in range(15):
			image.putpixel((a+x, b+y),(0, 0, 0))
def eye(a, b):
	for x in range(30):
		for y in range(75):
			image.putpixel((a+x, b+y), (0,0,0))

pixel(150, 300)
pixel(330, 300)
pixel(180, 330)
pixel(300, 330)
for x in range(165):
	for y in range(15):
		image.putpixel((165+x, 315+y), (0,0,0))
for x in range(105):
	for y in range(15):
		image.putpixel((195+x, 345+y), (0,0,0))
eye(195, 225)
eye(270, 225)




image.save("redpicture.png", "PNG")