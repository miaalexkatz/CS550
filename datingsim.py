# Mia Katz
# 9.24.18
# Text Based Adventure Game
#Description: The Winter Ball is in two days, and you still haven't found someone to go with yet! Luckily, you know three (and definitely only three, nobody else) attractive (and single) people who are conveniently in your homeroom! Can you persuade a someone into asking you out???? Welcome to DatingSim.py! There are four different endings, can you collect them all?
# Sources: All of the text art is from patorjk.com, but the heart is from fsymbols.com. Special thanks to Caroline Huber for playing this during her free block
#On my honor, I have neither given nor received unauthorized aid

def name():
	input("""
┌┬┐┌─┐┌┬┐┬┌┐┌┌─┐┌─┐┬┌┬┐ ┌─┐┬ ┬
 ││├─┤ │ │││││ ┬└─┐││││ ├─┘└┬┘
─┴┘┴ ┴ ┴ ┴┘└┘└─┘└─┘┴┴ ┴o┴   ┴ 
……..@*@*
….@*……..@* ………………………..@*
..@*……………@* ………………@*……..@*
.@*……………….@*……….@*……………..@*
@*…………………..@*…@*………………….@*
@*………………………*…………………….. @*
.@*……………………………………………. @*
..@*………………………………………..@*
….@*…………………………………..@*
……..@*…………………………..@*
………..@*…………………… @*
…………….@*…………..@*
……………….@*…… @*...........
………………….*@*..............

now with FOUR DIFFERENT ENDINGS!!!!
Press Enter to Start!
		""")
	start()

# this is the intro to the game
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
>>  """)
    while result != '1' and result!= '2' :
    	result = input("That's not valid, try again! >> ")
    if result == '1':
        hall()
    elif result == '2':
        school()

#the lead between the start and reading the ball poster
def hall():
    result = input("""
You make your way through the hallway, accidentally knocking over some freshman. 
But whatever. You made it. 
It's another one of those posters for a school dance.

What do you wish to do?
1) Read the Poster
2) Turn Away and Go to Class
>>  """)
    while result != '1' and result!= '2' :
    	result = input("That's not valid, try again! >> ")
    if result == '1':
        pickup()
    elif result == '2':
        school()
#The poster for the ball, leads into main class scene
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

>>  """)

    while result != '1' and result!= '2' :
    	result = input("That's not valid, try again! >> ")
    if result == '1':
        school()
    elif result == '2':
        print("""
Sadly, the hall monitor caught you. You're lucky to avoid detention.
        	""")
        school()

       #MAIN CLASS SCENE
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

>>  """)
    while result != '1' and result!= '2':
            result = input("That's not valid, try again! >> ")
    if result == '1':
        left()
    elif result == '2':
        right()
#division into james and harper routes
def left():
	result = input("""
Alright, who are you talking to? 
	
1)James or 
2)Harper?

>>  """)
	while result != '1' and result!= '2':
		result = input("That's not valid, try again! >> ")
	if result == '1':
		james()
	elif result == '2':
		harper()
#division into mango and other route
def right():
	result = input("""
Now's your chance to 

1)Talk to Mango or 
2) Be anti-social!

It's not up to me!
>>  """)
	while result != '1' and result!= '2':
		result = input("That's not valid, try again! >> ")
	if result == '1':
		mango()
	elif result == '2':
		truth()
#james route, leads from left()
def james():
    result = input("""
James seems to be pretty busy with that phone of his. It's up to you to make the first move.

What are you going to do?
1) Ask about his college plans
2) Congratulate him on the football team win
     
>>  """)
    while result != '1' and result != '2':
    	result = input("That's not valid, try again! ")
    if result == '1':
    	college()
    elif result == '2':
    	football()
#negative james route, leads to lonely() 
def college():
	print("""
You kindly ask him if he's thinking about college overseas.
And he's kind of upset.

"Why wouldn't I go in the USA?" he scoffs,
"Do you have something against our home??? OUR PRESIDENT?????"

You back up slowly. Oh god, what was that....
		
It's too bad humans are like that...

you don't need a boy to have a nice time at a dance now, do you?""")
	lonely()
#leads into positive james 
def football():
	result = input("""
"Hey, thanks," he smiles. It's a cute smile.
You give him an awkward thumbs up. (Don't worry, I'd do the same)

"Random, honest school spirit question," he starts.
"When you go to a sports game, what's the best part?"

What do you think is the best part?
1) The thrill of rooting for your team!
2) Nachos.
	
>>	""")
#this leads inot both game scene and improv scene
	while result != '1' and result != '2':
		result = input("That's not valid, try again! ")
	if result == '1':
		print("""
"Well, I'm playing Thursday night" he says, smirking at you. 
"Maybe you should check it out! And find me afterwards, cutie"

You mark it in your planner. Besides, homework can be done on bleachers, right?
			""")
		game()
	elif result == '2':
		print("""
He stares at you in disbelief.

"Wow... I thought someone like you would be thrilled to cheer on such a team..."
He picks up his phone again. You see he's reading old news.

The odd headlines are kind of making you uncomfortable.

"Whatever, I would've suggested you to the halftime squad but you're...
not even that pretty. Lol. I'm still a nice guy, though. A gentleman"

what... a... jerk...

Whatever. You should probably avoid football at all costs.
how about improv?
    """)
		improv()
#main harper route, can lead to all endings
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

>>  """)
	while result != '1' and result != '2':
		result = input("That's not valid, try again! ")
	if result == '1':
		hpop()
	elif result == '2':
		h2011()
#mango intro, leads to improv
def mango():
	result = input("""
Mango sees you approach, and acknowledges you with a smile. 
But then they return to their device, wildly pressing buttons. 

What are you going to say to them?
1) Ask about the weird device
2) Ugh. Who cares, they already ignored you once so what's the use?
	
>>	 """)
	while result != '1' and result!= '2':
		result = input("That's not valid, try again! ")
	if result == '1':
		mdevice()
	elif result == '2':
		mignore()
#
def mignore():
	print("""
Mango noticed you didn't smile back. If they're hurt, they aren't showing it well. 
Maybe they're too cool for that, you think. But whatever. Class is starting.
.
.
.
.
.

you'll be okay... 
I'm still here for you...

all of these other characters are overrated anyways...

	""")
	lonely()

#positive mango route
def mdevice():
	result = input("""
You ask Mango about their device. It's an iPhone !. Apple abandoning numbers?? That sounds crazy!
It has an unmatchable speed, and new capabilities in the internet category. 

Mango offers their phone to you, and tells you you use one app.

You pick:
1) Messages
2) Face Scanner 3D Model Replica

>>	 """)
	while result != '1' and result != '2':
		result = input("That's not right, try again! >> ")
	if result == '1':
		messages()
	elif result == '2':
		mangoevent()
#leads to improv, from device 
def mangoevent():
	result = input("""
"Oh my god... that's the newest addition!!!!" they exclaim.
They proceed to scan your face, and even ask if you're interested in 3D printing it
You pass, sice you're not sure you want a plastic version of your face.
But it's the thought that counts?

After the scan, they proceed to invite you to the improv show.
They're not performing, but enjoy live shows, and would love if you came along!
They said they'll even buy you some popcorn!

What do you say?
1) only if we get extra butter on the popcorn!!!
2) Sorry, I was kind of planning on going to the football game...
		""")
	while result != '1' and result != '2':
		result = input("That's not right, try again! >> ")
	if result == '1':
		improv()
	elif result == '2':
		game()
#if you get here you honestly deserve a bad ending cause you need to respect others... leads to football game
def messages():
    print("""
"What... the hell... is wrong with you!" Mango screams, taking their phone.
Yeaaaahhhh, maybe you shouldn't go through their personal conversations.
Especially since you don't have a date yet.
Maybe you'll have better luck finding someone at football!
    	""")
    game()
#leads to the football game
def h2011():
	result = input("""
Harper looks a bit dissatisfied. 

"That's not exactly new, but thanks anyways," she responds. 

She pulls out her laptop with her writing project on it, and proceeds to type furiously.
But your class is starting now. 

You feel really, really bad. 
Until James taps you on the shoulder and invites you to the football game!
It's not like you have anything better to do.""")
	game()

#leads to improv/goodend
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
#improv segway
def hinvite():
	print("""
"Awesome! I have an improv troupe tomorrow night!" she responds, smiling,
"It's our first performance of the year!"
You tell her you're going to check it out.
It's not like you have anything else to do.
	""")
	improv()
#MAIN FOOTBALL GAME leads to harper, badend and james 
def game():
	result = input("""
Location: Nova High School Fields
Time: 4:45 PM
Date: Thursday, December 12th
Pre-Game: WINTER BALL IS TOMORROW NIGHT! BUY TICKETS.... OHHHH SAY CAN YOUUUU SEEEEEEE...

Well, you made it through the sea of jerseys.
But you're here now! And you bought nachos.
(totally worth the price, if ya ask me)

You sit alone through most of the game, until someone you know shows up.

It's Harper, since the improv show must have ended.

Wanna go talk to her?
1) Yeah, I'm kinda lonely
2) No, I came to see James.

>>  """)
	while result != '1' and result != '2':
		result = input("That's not right, try again! >> ")
	if result == '1':
		harpergame()
	elif result == '2':
		jamesgame()
#from game(), to harper and badend()
def harpergame():
	result = input("""
Harper is surprised to see you here, but happy nonetheless!
She offers you a sip of her latte. It's alright, but you've never cared for pumpkin.

"So, are you going to the dance tomorrow?" she asks, 
"Y'know, the Winter Ball?"
You tell her you're not totally sure, but you don't have anyone to go with.

She smiles and sips her latte again. The team scores a touchdown.

BUT QUICK! Now's your chance!

1) Keep watching the game and sit there, awkwardly...
(idk, maybe there's... someone else?)
2) ASK!!! HER!!!! OUT!!!!

>>	""")
	while result != '1' and result != '2':
		result = input("That's not right, try again! >> ")
	if result == '1':
		badend()
	elif result == '2':
		askherout()
#harper good ending
def askherout():
	print("""
"Maybe you'd want to go to the dance with me?"
She smiles gleefully, and hugs you with much enthusiam.

You decide to leave the game and pick some outfits from the costume shop.

Location: Nova High School Cafeteria
Time: 7 PM
Date: Friday, December 13th

You both bike to the dance together. Harper insists, as she saw it on Pinterest.
The bikes are lined with flowers, and are outright beautiful. 

You don't think you've ever had this much fun with a girl at a dance.
She's living in the moment, unlike James or Mango.
He's stuck in the past. They're stuck in the future.

But you spend the night dancing, screaming karaoke, and eating cupcakes.
God, you really love cupcakes.

And together, you attend the Spring Fling dance. And the Summer Dance.
And next year's Homecoming. Winter Ball. Valentine's Dance.
Over and over and over and over.

Seven years later, you're still attending dances.
I mean, obviously not at a high school. But it's still fun.

And one day, you ask her if you want to attend dances forever.
And she says yes.

THE END
	""") 
#james asking out, neither ending is that good
def jamesgame():
	result = input("""
After the game, you down to the field. There he is! It's James!
He notices you arrive, but he's also pretty sweaty.

"Hey! Glad you could make it!" he cheers, placing his water bottle on a bench.

And you're glad you could make it too.

"Hey, listen... I've been meaning to ask you about the dance."
You ask for clarification.
"Would you maybe want to go with me?"

1) Yes
2) No

>>  """)
	while result != '1' and result != '2':
		result = input("That's not right, try again! >> ")
	if result == '1':
		jyes()
	elif result == '2':	
		jno()
#james ending... not the best
def jyes():
	print("""
Location: Nova High School Cafeteria
Date: Friday, December 13th

James picks you up in his car. It's not cheap by any means.
The two of you walk into the dance together, hand in hand

The dance is decorated with silver sparkles. There's even a wintry photo booth!

You take your pictures. You dance to the slow songs. 
You even talk to Harper and Mango for a bit. They're happy for you as well.

but most importantly,
you eat so many tacos you think you might explode.

And the two of you stay a couple for quite some time...

until the next election.

In the wake of the campaign, you check your Twitter feed.
Next thing you know, you're on the phone, sobbing.
You deserve better than someone who posts racist content. He calls you an SJW.
But you deserve someone who shows respect to everyone, no matter their standing

Maybe you should've known. But don't beat yourself up over it.
The best revenge is a life well lived

THE END
		""")
#leads to badend but at least the narrator isn't a trashy person
def jno():
	result = input("""
You reject him. He's devastated.

He leaves the bench, muttering something.
It's something about "good for nothing feminists"

You're probably better off.

What now?
1) Talk to Harper???
2) Talk to Mango???
3) talk... to someone you didn't think was an option?

>>   """)
	while result != '3':
		result = input ("no. >> ")
	if result == '3':
		badend()
#IMPROV MAIN DIVIDEND
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
	while result != '1' and result != '2':
		result = input("That's not right, try again! >> ")
	if result == '1':
		mimprov()
	elif result == '2':
		himprov()
#mango's divide from improv
def mimprov():
	result = input("""
Mango has a nice tub of popcorn with extra butter with them.
The bright yellow popcorn oddly compliments their mango colored hair. It's cute!
As you sit next to them, they tell you about their gift card habits.
"Always better to prepare for discounts in the future!" they say

The two of you sit together through the performace. 
It's surprisingly good, given that it's a group of teenagers. They earn a standing ovation.

"Oh... shoot," they spit, "dang it, I have to babysit at 7... 
it's at the park, there will be other sitters there... wanna come?"

What do you even respond to that?
1) "Yeah, sure! It'll be fun!"
2) "Sorry, you should be responsible..."

>>  """)
	while result != '1' and result != '2':
		result = input("That's not right, try again! >> ")
	if result == '1':
		babysitting()
	elif result == '2':
		responsibility()
#leads to mango asking out
def babysitting():
	result = input("""
Yeah, you're not totally sure why you chose to go to the park.
But maybe you'll be paid!!!!!

There are only a few kiddos there, all younger than 7.
They frolick on the playground, and are all smiles! They make you happy too!

But it only gets better after they leave.
You and Mango trek to the ice cream parlor, and they offer to pay.
You sit on a park bench together with your sweets. 
It's peaceful.
It's tranquil.
And you watch the pale sunset on the horizon.

As they finish up their cone, they turn to you, and you know what they're about to say.
"Are you free for the Winter Ball tomorrow night?"

1) Yes
2) No

>>  """)
	while result != '1' and result != '2':
		result = input("That's not right, try again! >> ")
	if result == '1':
		myes()
	elif result == '2':
		print("""
"Oh... you must be going with someone else then. I hope you have a nice time..."
and they turn away after you get home safely.

So why didn't you say yes?
You're not falling for someone else, right?
Someone who wouldn'nt ever desert you? Who's been here the whole time?
			""")
		badend()
#mango ending, pretty good
def myes():
	print("""
They smile back, take your hand, and walk you home.
They walk you down the spiraling sidewalks of Nova City.
Honestly, you'd be fine not even going home at all. But still, morning comes.

Location: Nova High School Cafeteria
Time: 7 PM
Date: Friday, December 13th

You walked the sidewalks again to arrive to the snowy dance.
"Dang, that's a lot of streamers," they gasp.
Everything is twnkling in blues and whites, and it's breathtaking.

Though you're more laid back, you still have an amazing time.
You grab cupcakes, and huddle around the standing tables, and just talk.
They talk about their struggles with mental health, and finding a support system.
You talk about this weird schizophrenic voice that's been narrating you.

But overall, it's a charming time you won't forget.

As for your future? The two of you last until your first year of college.
They're just so future focused, and you don't blame them.
Even though you enjoyed all of your dates, you realize that spark is gone.
But it's okay, and you keep a close friendship throughout your adult lives.
You even give a speech at their wedding!

Even though things didn't work out romantically, you still treasure the company

THE END
		""")
#badend ending
def responsibility():
	result = input("""
"Yeah... you're probably right..." they answer. 
You apologize. They tell you not to.

They leave the auditorium, but daaaaaaang was that impulsive.
Maybe it's best that it didn't go anywhere.

But now what do you do?
1) Find Harper, and congratulate her!
2) Find James
3) find someone super special who will support you ALWAYS in life~

>>  """)
	while result != '3':
		result = input("there's someone better.... try again ;) >> ")
	if result == '3':
		print("yay! you picked ME! :)")
		badend()
#leads to askherout aka best ending
def himprov():
	result = input("""
And with that, you're sitting alone...
Oh well, it's for a good cause?
At least her performance was amazing, and so in-the-moment!

After the show, you head backstage to where Harper is. She's thrilled to see you here!
Someone already gave her flowers, and you're a bit worried.
So you ask about them.
But she assures you that they're from her mom.

You also brought her a flower! It's a daffodil, and it's in full bloom.
And the two of you hug, and you say...

1) "You were really great, nice job!"
2) something about the winter ball?
>>  """)
	while result != '1' and result != '2':
		result = input("That's not right, try again! >> ")
	if result == '1':
		print("""
And she smiles, although disappointedly...
C'mon.... your chance was right there
And now you're alone and lonely, as she leaves with her mom.

But what do you do now?
1)Talk to James????
2) Mango?????
3) talk to someone better, who's been here the whole time, guiding you? Who really cares????
>>	""")
		while result != '3':
			result = input("that's not what is advised, honey-sweetie-pie... >> ")
		if result == '3':
			badend()
	elif result == '2':
		askherout()
#if you really messed up in the first scene, you'll end here
def lonely():
	print(""" 
Location: Nova High School Parking Lot
Date: Wednesday, December 11th
Time: 3 PM

Ugh. You were about to drive home, when your car decides to break down. 
So now you're stuck here.
Might as well make the best of it and talk to me... """)
	badend()
#the not very good ending which mostly means you failed
def badend():
	result = input("""
I know I'm not the most desirable kid here...
but I'm still here?

And I'm not going to the dance with anyone...
and you're not going to the dance with anyone...

and maybe you should go with me? 

So yeah. I'm asking you out. 
Choose wisely.
1) YES, MY BEAUTIFUL NARRATOR, I WILL!
2) I think I might look for another classmate
3) I'm fine on my own
4) I don't know, maybe I should ask Harper
5) And maybe Mango? They're cute too
6) But there's always James
7) Actually, I was thinking of just going on my own...

>>	""")
	while result != '1' :
		result = input("u n a c c e p t a b l e. >> ")
	if result == '1':
		fty()
#the inputs here mean nothing. you have no control, but it's okay.
def fty():
	input("""

I show up to your house in a beautiful carraige!
y o u ' r e    r o y a l t y    n o w!!!!!!!!!!!!!!!!!!!!!

And we get to the dance! And it's just us!!!!

isn't that...
r o m a n t i c???

answer, you peasant.
>>  """)
	input("""
I agree! It's sooooooo romantic!
I've never been to a dance with anyone before...
I'm really loving it!

oh my gosh, a slow song???? I love this song!

C'mon, let's dance! It'll be so magical!!!! 

Will you dance with me???

>>  """)


	input("""And I take your hand and we dance and it's nice but you'll never be as good as I AM.
it's okay, I'll still love you!!!!

And together, we finish high school!!!!
and somehow, I'm also accepted into your college!

I... m i s s e d    y o u!!!!!!
So much!!!!!!!!!!!!!!

did you miss me too?

>> 	""")

	input("""
Oh, I knew you'd miss me too! And now you're right here!
On this campus with me!!!!!!!!!!

and then we graduate and now we don't even have classmates
and there's n o   getting d is tracted!!!!!

but one day, we're on a beach. And I know there's something....
s o me t hing you want me to kn o w????

It's a question!!!! I know that for sure!!!!!
f o u r w o r d s, h u h?

just say it... i know you want to
>>  """)

	print("Yes! Yes, I'll marry you! We'll be together!!!! for-e-ver ;) THE END!!!!!!!!!!!!!!")
#truth or dare segment
def truth():
    result = input("""
Oh... okay. Well, you're not sitting here doing nothing. 
Wanna play a game? 
1) yes
2) no?

>>  """)

    if result == '2':
    	result = input("""
fine... I see how it is. We're not friends.
Just leave me alone. I'm hurt. I'm done personalizing this question.

1) Go to improv.
2) Go to football.
    		""")
    	while result != '1' and result != '2':
    		print("you want to hurt me with a wrong value too??? >>")
    	if result == '1':
    		improv()
    	elif result == '2':
    		game()

    elif result == '1':
    	result = input("""
1) Truth or 2) dare?
""")
    	if result == '1':
    	    result = input("Okay, give me your darkest secret!!!! ")
    	    print("""
Well, I wasn't really expecting anything at all. But your class is starting. 
And you're not sitting home alone tonight. 

So I dare you to go to the football game or the improv show!
1)Football
2)Improv
>>  """)
    	    while result != '1' and result != '2':
    	    	result = input("That's not right, try again! >> ")
    	    if result == '1':
    	    	print("as my mom says, ARE YOU READY FOR SOME FOOTBALL")
    	    	game()
    	    elif result == '2':
    	    	print("hope ya like improv!")
    	    	improv()

    	elif result == '2':
    		result = input("""
Well, I DARE YOU to go to an event!!!! 
1) Football or
2) The improv show!!!
They're both at the same time, though	     

>>  """)
    		while result != '1' and result != '2':
    			result = input("It's not gonna kill you to choose >> ")
    		if result == '1':
    			game()
    		elif result == '2':
    			improv()
    	else:
    		print("fine, I'll live. But you've disappointed me. That's sad... just leave me alone, I don't know go to improv or something")
    		improv()
#*slaps roof of function* this bad boy can fit so many game start screens in it
name()
