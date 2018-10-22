#Mia Katz
#10.24.18
#Fractals Project
#Sources: https://lodev.org/cgtutor/juliamandelbrot.html for learning what the Julia set actually is

from PIL import Image
import colorsys
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

d = 0.2314190881763527 
e = - 0.5322770541082162
c = complex(d,e)
xa, xb = .245, .345
ya, yb = 0.813, 0.913
maxIt = 256
cy = 0
cx = 0
for y in range(imgy):
	cy = y * (yb-ya)/(imgy-1) + ya
	for x in range(imgx):
		cx = x * (xb-xa)/(imgx-1) + xa
		z = complex(cx, cy)
		for i in range(maxIt):
			if abs(z) >= 2.0:
				break
			z = z**2 + c
		julia.putpixel((x,y),(colorsys.rgb_to_hsv(i, 100, 50)))
print("Julia Complete")

image.show()
julia.show()