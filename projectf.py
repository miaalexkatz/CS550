#Mia Katz
#10.24.18
#Fractals Project
#The first project is a Mandelbrot, with an ombre pattern replacing anywhere that doesn't escape. It is layered with a small checkerboard for an added effect.
#The second is a Julia with a blurred filter over it. It also has some alternating color stripes
#The third is a mandelbrot divided into four squares. Two of them are very patterned, and the other two have a gradient and a smoothing filter over them!
#Sources: https://lodev.org/cgtutor/juliamandelbrot.html for learning what the Julia set actually is, https://docs.python-guide.org/scenarios/imaging/ for help with Filters, and https://pillow.readthedocs.io/en/5.2.x/reference/ImageFilter.html for even more about the filters. https://www.atopon.org/mandel/# for the zooms on the mandelbrot, and https://www.cs.unm.edu/~stharding/julia/julia.html for the Julia shapes!

from PIL import Image, ImageFilter
xa, xb = 0.3038888888, 0.35888888
ya, yb = 0.545, 0.6
jxa, jxb = -0.6, 0.4
imgx, imgy = 512, 512

maxIt = 256

image = Image.new("RGB", (imgx, imgy))
julia = Image.new("RGB", (imgx, imgy))
two = Image.new("RGB", (imgx, imgy))

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
		if x< 103 or 206<=x<306 or x>409:
			julia.putpixel((x,y),(i, 12, (i*68)%256))
		else:
			julia.putpixel((x,y), (i*68%256, i, 12))

print("Julia Complete")

xa, xb = -1.9425254, -1.9425244
ya, yb = -0.0000132425, -0.000012279805

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
		if (x > 256 and y > 256) or (x<256 and y<256):
			two.putpixel((x, y), ((i*48)%256, (i*1982)%256, int(x/2)))
		else:
			two.putpixel((x,y), (i, int(y/2), int(x/2)))

	   
print("Done!")
ju = julia.filter(ImageFilter.BLUR)
image.show()
ju.show()
tu = two.filter(ImageFilter.SMOOTH)
tu.show()