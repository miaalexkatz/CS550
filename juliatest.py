from PIL import Image 
import random
imgx, imgy = 512, 512


julia = Image.new("RGB", (imgx, imgy))
d = 0.2314190881763527 
e = - 0.5322770541082162
c = complex(d,e)
xa, xb = .245, .345
ya, yb = 0.813, 0.913
maxIt = 256

for y in range(imgy):
	cy = y * (yb-ya)/(imgy-1) + ya
	for x in range(imgx):
		cx = x * (xb-xa)/(imgx-1) + xa
		z = complex(cx, cy)
		for i in range(maxIt):
			if abs(z) >= 2.0:
				break
			z = z**2 + c

		julia.putpixel((x, y), ((i*12)%256, i, (i*86)%256))

julia.show()