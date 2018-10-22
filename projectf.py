#Mia Katz
#10.24.18
#Fractals Project
#Sources: https://lodev.org/cgtutor/juliamandelbrot.html for learning what the Julia set actually is

from PIL import Image

xa, xb = 0.3038888888, 0.35888888
ya, yb = 0.545, 0.6
jxa, jxb = -0.6, 0.4
imgx, imgy = 512, 512

maxIt = 256

image = Image.new("RGB", (imgx, imgy))
julia = Image.new("RGB", (imgx, imgy))

for y in range(imgy):
	cy = y * (yb-ya)/(imgy-1) + ya
	for x in range(imgx):
		cx = x * (xb-xa)/(imgx-1) + xa
		c = complex(cx, cy)
		z = 0
		for i in range(maxIt):
			if abs(z) >= 2.0:
				break
			z = z**2 + c
		
		if (x%2 == 0 and y%2 == 0) or (x%2 != 0 and y%2 != 0):
			if 254 > i:
				image.putpixel((x, y), ((i*6)%256, i, 50))
			else:
				image.putpixel((x, y), (int(y/2), int((y+x)/4), int(x/2)))
		elif 254< i:
			image.putpixel((x,y), (int(x/2), 0, int(y/2)))
		else:
			image.putpixel((x, y), ((i*12)%256, i, (i*86)%256))
print("Mandelbrot 1 Complete")


for x in range(imgx):
	jx = 1.5*(x - imgx/2)/(0.5*5*imgx) + 7
	for y in range(imgy):
		jy = 1.1*(y -imgy/2)/(imgy*0.5*5) + 8
		j = complex(jx, jy)
		for i in range(maxIt):
			if jx*jx + jy*jy > 4 and i>1:
				break
			cat = jx*jx - jy*jy + jxa
			jy,jx = 2.0*jx*jy + jxb, cat 
		julia.putpixel((x, y), (0, i*36%256, i*672%256))

#for y in range(imgy):
#	jy = y/imgy
#	for x in range(imgx):
#		jx = x/imgx
#		jo = complex(jx, jy)
#		for i in range(maxIt):
#			if abs(jo) >= 2:
#				break
#			jo = jo**2 + j
#		image.putpixel((x, y), (0, i, 0))

		#else:
		#	image.putpixel((x,y), ((i*12)%256, i, (i*86)%256))


image.show()
julia.show()