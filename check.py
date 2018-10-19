from PIL import Image

imgx = 512
imgy = 512
image = Image.new("RGB", (imgx, imgy))
for x in range(imgx):
	for y in range(imgy):
		image.putpixel((x,y),(0,0,0))
		
for x in range(0, imgy, 128):
	for y in range(0, imgx, 128):
		for z in range(64):
			for a in range(64):
				image.putpixel((z+x,a+y), (255,0,0))

for x in range(0, imgy, 128):
	for y in range(0, imgx, 128):
		for z in range(64):
			for a in range(64):
				image.putpixel((z+x+64,a+y+64), (255,0,0))











image.save("check.png", "PNG")