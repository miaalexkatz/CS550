#def check(result,1,2):
 #   while result!=1 and result!=2:
  #  	result = input("Please pick an actual option! >> ")
   # return result
detentions = 0
mango = 0
harper = 0
james = 0
narrator = 0
def name():
	name = input("Enter your Name: ")
	start()

def start():
    print("Student ID:",name)
    result = input("""
Location: Nova High School
Date: Monday, December 11th

It's early in the morning, but the halls are already packed. You're at your locker, staring out into the sea  
of students, when you notice something:
It's a small cluster of students gathered on the oppposite side!

     What do you wish to do? 
     1) Go over to the cluster
     2) Go to class
     >> """)

    #if check(result,1,2) == 1:
    while result != '1' and result!= '2' :
    	result = input("That's not valid, try again! >> ")
    if result == '1':
        hall()
    elif result == '2':
        school()

def hall():
    result = input("""
You make your way through the hallway, accidentally knocking over some freshman. 
But whatever. You made it. 

It's another one of those posters for a school dance.

    	What do you wish to do?
    	1) Read the Poster
    	2) Turn Away and Go to Class
    		""")
    while result != '1' and result!= '2' :
    	result = input("That's not valid, try again! >> ")
    if result == '1':
        pickup()
    elif result == '2':
        school()

def pickup():
    result = input("""
    . , , . ,-. |- ,-. ,-.   |-. ,-. |  |  
    |/|/  | | | |  |-' |     | | ,-| |  |  
    ' '   ' ' ' `' `-' '     ^-' `-^ `' `' 
    * - _ - * - _ - * - _ - * - _ - * - _ - *

    The winter ball is this FRIDAY NIGHT!

        Anyone can ask anybody! 

    The ball will be in the auditorium

    Music provided by Anxiety! at the Dance

            FREE ADMISSION 
    
    ________________________________________

    Suddenly, the school bell rings. What do you do?
    1) Go to class, because you are dependable 
    2) Skip, cause you're cool B)       

    >> """)

    while result != '1' and result!= '2' :
    	result = input("That's not valid, try again! >> ")
    if result == '1':
        school()
    elif result == '2':
        print("""
    Sadly, the hall monitor caught you. That's one detention strike...
    Three means you can't go to the Winter Ball!
        	""")
        school()

def school():
    result = input("""
    You open the door to your homeroom. Only three people are here!
    Lucky for you, they're popular and available 

    First, there's James, a classic guy who plays football in his spare time.
    He's scrolling through his messages on his phone 

    Next, there's Harper. She's both current and nostalgic, in a way... 
    She's listening to her Radio Hits playlist

    And lastly, there's Mango. They're the trendiest of the three, with new gadgets
    They have some device in their hand, but you honestly have no idea what it is.

    Mango and an empty desk are on the right.
    James and Harper are on the left side of the room.

    Where do you go?
    1) Left (James and Harper)
    2) Right (Mango and Being Anti Social)

    	""")
    while result != '1' and result!= '2':
            result = input("That's not valid, try again! >> ")
    if result == '1':
        left()
    elif result == '2':
        right()

def left():
	result = input("""Alright, who are you talking to? 
		1)James or 
		2)Harper?

		>> """)
	while result != '1' and result!= '2':
		result = input("That's not valid, try again! >> ")
	if result == '1':
		james()
	elif result == '2':
		harper()

def right():
	result = input("""Now's your chance to 
		1)Talk to Mango or 
		2) Be anti-social!

		It's not up to me!
		>> """)
	while result != '1' and result!= '2':
		result = input("That's not valid, try again! >> ")
	if result == '1':
		mango()
	elif result == '2':
		truth()

def james():
    input("""
    	James seems to be pretty busy with that phone of his. It's up to you to make the first move.

    	What are you going to do?
    	1) Ask about his college plans
    	2) Congratulate him on the football team win
     
     >> """)

def harper():
	input("""
	Though Harper is listening to music, she immediately notices you approach her and removes her headphones. How nice!

	"Hey, """ +name+"""!" she says, "How's your day going?"

	You tell her it's been fine, though not very eventful.

	"Yeah, same here. Anyways, I've been wondering, do you happen to have any music recs? 

	She's scrolling through her playlist now. It's full of catchy songs you heard about twelve times on your drive here.
	
	"I'm always looking for something new to enjoy!"

	What dd you recommend to her?
	1) A day-old single from one of your favorite bands
	2) Your favorite 2011 radio hit
		
    >> """)

def mango():
	result = input("""
    Mango sees you approach, and acknowledges you with a smile. 
    But then they return to their device, wildly pressing buttons. 

    What are you going to say to them?
    1) Ask about the weird device
    3) Ugh. Who cares, they already ignored you once so what's the use?
		
	>>	""")
	while result != '1' and result!= '2':
		result = input("That's not valid, try again! ")
	if result == '1':
		mdevice()
	elif result == '2':
		mignore()
    #elif result == '3':
       # mdevice()

def mignore():
	mango -= 2
	result = print("Mango noticed you didn't smile back. If they're hurt, they aren't showing it well. Maybe they're too cool for that, you think. But whatever. Class is starting.")

def mdevice():
	result = input("""
    You ask Mango about their device. It's an iPhone !. Apple abandoning numbers?? That sounds crazy!
    It has an unmatchable speed, and new capabilities in the internet category. 

    Mango offers their phone to you, and tells you you use one app.

    You pick:
    1) Messages
    2) Face Scanner 3D Model Replica

	>>	""")

def truth():
    result = input("""
    		Oh... okay. Well, you're not sitting here doing nothing. 
    		Wanna play a game? 
    		yes, or no?""")

    if result == 'yes':
    	narrator += 1
    	result = input("Truth or dare?")
    	if result == 'truth':
    	    narrator += 1
    	    input("Okay, give me your darkest secret!!!! ")
    	    print("Well, I wasn't really expecting anything at all. But your class is starting.")
    	elif result == 'dare':
    	    narrator += 1
    	    input("""
    	           Well, I dare you to stop being anti-social. Pick someone to talk to, now.

    	           1) James
    	           2) Harper
    	           3) Mango
    	                      """)
    	else: 
    	    narrator -= 1
    	    print("Okay, fine. Guess you really don't care...")
    else:
    	narrator -= 1
    	print("fine, I'll live")

name()
