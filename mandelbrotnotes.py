from PIL import Image
imgx = 512
imgy = 512

image = Image.new("RGB", (imgx, imgy))

for x in range(imgx):
	for y in range(imgy):
		checks = 0
		cx = ((x/imgx)*4)-2
		cy = ((y/imgy)*4)-2
		zx = 0
		zy = 0
		for i in range(256):
			valuez = (zx**2)-(zy**2) 
			valuey = 2*zx*zy 
			ezx = valuez + cx
			ezy = valuey + cy
			if ((ezx**2)+(ezy**2))**(1/2) >= 2:
				image.putpixel((x,y), (50, checks, 50))
				break
			if checks == 255:
				image.putpixel((x,y), (50, checks, 50))
				break
			else:
				zx = valuez
				zy = valuey
				checks += 1

image.save("ruby.png", "PNG")