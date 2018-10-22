from PIL import Image
imgx = 512
imgy = 512

mandelbrot = Image.new("RGB",(imgx, imgy))

for x in range(imgx):
	for y in range(imgy):
		check = 0
		zx = 0
		zy = 0
		cx = ((x/imgx)*4)-2
		cy = ((y/imgy)*4)-2
		while True:
			if check == 255:
				break
			valuez = (zx**2)-(zy**2)
			valuey = 2*zx*zy
			ezx = valuez + cx
			ezy = valuey + cy
			if ((ezx**2)+(ezy**2))**(1/2) > 2:
				break
				print("working")
			else:
				zcx = ezx
				zcy = ezy
				check += 1
		mandelbrot.putpixel((x,y),(check,0,check))

mandelbrot.save("boi.png","PNG")