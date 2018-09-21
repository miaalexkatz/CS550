#def check(result,1,2):
 #   while result!=1 and result!=2:
  #  	result = input("Please pick an actual option! >> ")
   # return resul

def name():
	input("Press Enter to Start!")
	start()

def start():
    result = input("""
Location: Nova High School Hallways
Date: Wednesday, December 11th
Time: 7:54 AM

It's early in the morning, but the halls are already packed. 
You're at your locker, staring out into the sea of students, when you notice something:
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
Sadly, the hall monitor caught you. You're lucky to avoid detention.
        	""")
        school()

def school():
    result = input("""
Location: Nova High School: Room 103
Date: Wednesday, December 11th
Time: 7:58 AM
LOUDSPEAKER: TICKETS TO THE WINTER BALL ON FRIDAY WILL BE AVAILABLE AT LUNCH!

You open the door to your homeroom. Only three people are here!
Lucky for you, they're popular 

(and available!) 

First, there's James, a classic guy who plays football in his spare time.
He's scrolling through his messages on his phone 

Next, there's Harper. She's both current and nostalgic, in a way... 
She's listening to her Radio Hits playlist

And lastly, there's Mango. They're the trendiest, with new gadgets
They have some device in their hand, but you honestly have no idea what it is.

Mango and an empty desk are on the right.
James and Harper are on the left side of the room.

Where do you go?
1) Left (James and Harper)
2) Right (Mango and Being Anti Social)

    >>	""")
    while result != '1' and result!= '2':
            result = input("That's not valid, try again! >> ")
    if result == '1':
        left()
    elif result == '2':
        right()

def left():
	result = input("""
Alright, who are you talking to? 
	
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
	result = input("""
Now's your chance to 

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
    result = input("""
James seems to be pretty busy with that phone of his. It's up to you to make the first move.

What are you going to do?
1) Ask about his college plans
2) Congratulate him on the football team win
     
>> """)
    while result != '1' and result != '2':
    	result = input("That's not valid, try again! ")
    if result == '1':
    	college()
    elif result == '2':
    	football()

def college():
	print("""
You kindly ask him if he's thinking about college overseas.
And he's kind of upset.

"Why wouldn't I go in the USA?" he scoffs,
"Do you have something against our home??? OUR PRESIDENT?????"

You back up slowly. Oh god, what was that....
		""")
	lonely()

def football():
	input("""
"Hey, thanks," he smiles. It's a cute smile.
You give him an awkward thumbs up. (Don't worry, I'd do the same)

"Random, honest school spirit question," he starts.
"When you go to a sports game, what's the best part?"

What do you think is the best part?
1) The thrill of rooting for your team!
2) Nachos.
	
>>	""")
	while result != '1' and result != '2':
		result = input("That's not valid, try again! ")
	if result == '1':
		college()
	elif result == '2':
		print("""
He stares at you in disbelief.

"Wow... I thought someone like you would be thrilled to cheer on such a team..."
He picks up his phone again. You see he's reading old news.

The odd headlines are kind of making you uncomfortable.

"Whatever, I would've suggested you to the halftime squad but you're...
not even that pretty. Lol."

what... a... jerk...
    """)
		lonely()
def harper():
	result = input("""
Though Harper is listening to music, she immediately notices you and removes her headphones.
How nice!

"Hey," she says, "How's your day going?"
You tell her it's been fine, though not very eventful.

"Yeah, same here. Anyways, I've been wondering, do you happen to have any music recs? 

She's scrolling through her playlist now. 
It's full of catchy songs you heard about twelve times on your drive here.
	
"I'm always looking for something new to enjoy!"

What dd you recommend to her?
1) A day-old single from one of your favorite bands
2) Your favorite 2011 radio hit

	>> """)
	while result != '1' and result != '2':
		result = input("That's not valid, try again! ")
	if result == '1':
		hpop()
	elif result == '2':
		h2011()

def mango():
	result = input("""
Mango sees you approach, and acknowledges you with a smile. 
But then they return to their device, wildly pressing buttons. 

What are you going to say to them?
1) Ask about the weird device
2) Ugh. Who cares, they already ignored you once so what's the use?
	
>>	""")
	while result != '1' and result!= '2':
		result = input("That's not valid, try again! ")
	if result == '1':
		mdevice()
	elif result == '2':
		mignore()

def mignore():
	result = input("""
Mango noticed you didn't smile back. If they're hurt, they aren't showing it well. 
Maybe they're too cool for that, you think. But whatever. Class is starting.

	""")
	lonely()


def mdevice():
	result = input("""
You ask Mango about their device. It's an iPhone !. Apple abandoning numbers?? That sounds crazy!
It has an unmatchable speed, and new capabilities in the internet category. 

Mango offers their phone to you, and tells you you use one app.

You pick:
1) Messages
2) Face Scanner 3D Model Replica

	>>	""")

def messages()
    print("""
"What... the hell... is wrong with you!" Mango screams, taking their phone.
Yeaaaahhhh, maybe you shouldn't go through their personal conversations.
Especially since you don't have a date yet.
    	""")
    lonely()

def h2011():
	result = input("""
Harper looks a bit dissatisfied. 

"That's not exactly new, but thanks anyways," she responds. 

She pulls out her laptop with her writing project on it, and proceeds to type furiously.
But your class is starting now. 
		""")

def hpop():
	result = input(""" 
Harper exclaims that she's never heard of such a group before! 

As she's adding it, she asks if you're open to trying new things.

What do you say back?
1) "Yeah, always! What for?"
2) "sorry, no, my schedule's kinda packed."
		
	>>	""")
	while result != '1' and result != '2':
		result = input("That's not right, try again! >> ")
	if result == '1':
		hinvite()
	elif result == '2':
		print(""" 
"Oh... that's fine, the offer still stands..." Harper says. 
But she's clearly disappointed. 
Oh well... time for class.

	""")
		lonely()

def hinvite():
	print("""
"Awesome! I have an improv troupe tomorrow night!" she responds, smiling,
"It's our first performance of the year!"
You tell her you're going to check it out.
It's not like you have anything else to do.
	""")
	improv()
def game():
	result = input("""
Well, you made it through the sea of jerseys.
But you're here now! And you bought nachos.

You sit alone through most of the game, until someone you know shows up.

It's Harper, and the football game must have ended.

Wanna go talk to her?
1) Yeah, I'm kinda lonely
2) No, I came to see James.

 >> """)

def improv():
	result = input("""
Location: Nova High School Auditorium
Date: Thursday, December 12th
Time: 4:15 PM

You arrive at the auditorium, and it's a full house.
For a Thrusday night, there sure are a lot of students here.
You didn't come with anyone, but you're excited to see Harper.

However, you see a familiar face walk in!
It's Mango!

Do you want to sit with them?
1) Yeah, sure!
2) No, I came here to see Harper

	>>  """)

def lonely():
	result = input(""" 
Location: Nova High School Parking Lot
Date: Wednesday, December 11th
Time: 3 PM

Ugh. You were about to drive home, when your car decides to break down. 
So now you're stuck here.
Might as well make the best of it and attend an event...

There are two event slots tonight: 4:30 events and 6:30 events
But you can only go to one, since you have a TON of homework.

You glance at the schedule:
4:30: 
Improv Performance (with Harper!)
Football, Nova vs Paine (with James!)

6:30: 
Publications Meeting (with Mango!)
Gardening Club (who knows???)

Which Event Slot will you go to?
1) 4:30 events
2) 6:30 events

>>	""")
	while result != '1' and result != '2':
		result = input("That's not valid, try again! ")
	if result == '1':
		fty()
    elif result == '2':
    	sty()

def fty():
	result = input("""
You write down Homework @ 6:30 in your planner.

But now what?
1) Improv
2) Football

>>	""")

def sty():
	result = input("""
You sit down to work on a presentation.

But now what?
1) Publications
2)Gardening

		""")

def truth():
    result = input("""
Oh... okay. Well, you're not sitting here doing nothing. 
Wanna play a game? 
1) yes
2) no?

>> """)

    if result == '1':
    	result = input("""
1) Truth or 2) dare?
""")
    	if result == '1':
    	    input("Okay, give me your darkest secret!!!! ")
    	    print("Well, I wasn't really expecting anything at all. But your class is starting.")
    	elif result == '2':
    	    print("""
Well, I'd dare you to stop being anti-social. 
But it's time for class.
    	                      """)
    	    lonely()
    	else: 
    	    print("Okay, fine. Guess you really don't care...")
    	    lonely()
    else:
    	print("fine, I'll live")
    	lonely()

name()
