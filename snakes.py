from PIL import Image
import random as rd

imgx = 512
imgy = 512
image = Image.new("RGB", (imgx, imgy))
for x in range(imgx):
	for y in range(imgy):
		image.putpixel((x,y),(0,0,0))
snakenum = 65
r= 0
g = 0
b = 0
lol = 0
global turn
global snakey
turn = 0


def pr():
	global turn, snakey
	turn = snakey

for x in range(snakenum):
	snakey = 0
	r = rd.randrange(255)
	g = rd.randrange(255)
	b = rd.randrange(255)
	snakex = rd.randrange(imgx)
	
	for x in range(3000):
		if snakey <= 510:
			lol = rd.randrange(10)
			if lol < 2:
				if snakex != 0:
					snakex -= 1
				else:
					if snakey < imgy:
						snakey +=1
				image.putpixel((snakex, snakey),(r,g,b))
				pr()
			elif lol > 7:
				if snakex != imgx:
					snakex += 1
				else:
					if snakey < imgy:
						snakey += 1
				image.putpixel((snakex, snakey),(r,g,b))
				pr()
			else:
				if snakey < imgy:
					snakey += 1
				image.putpixel((snakex, snakey),(r,g,b))
				pr()

image.save("snake.png", "PNG")