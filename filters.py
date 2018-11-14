from PIL import Image
import random

un = Image.open("cav.jpg")
width, height = un.size
use = Image.new("RGB", (width, height))
pix = un.load()
print(height)
first = random.randrange(0, int(height/3), 1)
second = random.randrange(first, int(height/2), 1)
third = random.randrange(second, int((height/3))*2, 1)
fourth = random.randrange(third, int((height/5)*4), 1)
fifth = random.randrange(fourth, int((height/8)*7), 1)
sixth = random.randrange(fifth, height, 1)

print(first,second,third,fourth,fifth)

numb = random.randrange(0, 3)
for z in range(width):
	for i in range(first):
		RGB = pix[z,i]
		R,G,B = RGB
		oR = .900*R
		oG = .614*G
		oB = .272*B
		if oR < 255:
			oR = int(oR)
		else:
			oR = 255
		if oG < 255:
			oG = int(oG)
		else:
			oG = 255
		if oB < 255:
			oB = int(oB)
		else:
			oB = 255
		use.putpixel((z,i), (oR, oG, oB))
print("one")
numb = random.randrange(0, 3, 1)
for z in range(width):
	for i in range(first, second):
		RGB = pix[z,i]
		R,G,B = RGB
		oR = .793*R
		oG = .149*G
		oB = .382*B
		if oR < 255:
			oR = int(oR)
		else:
			oR = 255
		if oG < 255:
			oG = int(oG)
		else:
			oG = 255
		if oB < 255:
			oB = int(oB)
		else:
			oB = 255
		if z+100 < width:
			use.putpixel((z,i), (oR, oG, oB))
		#print(oR,oG,oB)
print("two")
for z in range(width):
	for i in range(second, third):
		RGB = pix[z,i]
		R,G,B = RGB
		oR = .723*R
		oG = .886*G
		oB = .392*B
		if oR < 255:
			oR = int(oR)
		else:
			oR = 255
		if oG < 255:
			oG = int(oG)
		else:
			oG = 255
		if oB < 255:
			oB = int(oB)
		else:
			oB = 255
		use.putpixel((z,i), (oR, oG, oB))
		#print(oR,oG,oB)
print("three")
numb = random.randrange(0, 3,1)
for z in range(width):
	for i in range(third, fourth):
		RGB = pix[z,i]
		R,G,B = RGB
		oR = .223*R
		oG = .623*G
		oB = .242*B
		if oR < 255:
			oR = int(oR)
		else:
			oR = 255
		if oG < 255:
			oG = int(oG)
		else:
			oG = 255
		if oB < 255:
			oB = int(oB)
		else:
			oB = 255
		use.putpixel((z,i), (oR, oG, oB))
print("four")
for z in range(width):
	for i in range(fourth, fifth):
		RGB = pix[z,i]
		R,G,B = RGB
		oR = .923*R
		oG = .983*G
		oB = .712*B
		if oR < 255:
			oR = int(oR)
		else:
			oR = 255
		if oG < 255:
			oG = int(oG)
		else:
			oG = 255
		if oB < 255:
			oB = int(oB)
		else:
			oB = 255
		if z+50 < height:
			use.putpixel((z+20,i), (oR, oG, oB))
		else:
			use.putpixel((z, i), (R, G, B))
for z in range(width):
	for i in range(fifth, height):
		RGB = pix[z,i]
		R,G,B = RGB
		oR = .237*R
		oG = .123*G
		oB = .242*B
		if oR < 255:
			oR = int(oR)
		else:
			oR = 255
		if oG < 255:
			oG = int(oG)
		else:
			oG = 255
		if oB < 255:
			oB = int(oB)
		else:
			oB = 255
		use.putpixel((z,i), (oR, oG, oB))
use.show()





