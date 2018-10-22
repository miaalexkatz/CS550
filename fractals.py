from PIL import Image

#xa, xb = -1.773660804, -1.7736607983
#ya, yb = 0.0063128809733, 0.006312884305
xa, xb = -2, 2
ya, yb = -2, 2

imgx, imgy = 512, 512

maxIt = 256

one = Image.new("RGB", (imgx, imgy))

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
		
		if i < 255:
			one.putpixel((x,y), ((i*12)%256, i, (i*86)%256))
		else:
			one.putpixel((x, y), (20, 0, int((y/2)%256))

one.show()

