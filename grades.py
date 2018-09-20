#Mia Katz 9.17.18
#The program that tells you your letter grade based on the number you input
#I didn't use any sources for this, though I tried to condense it as much as possible. The biggest challenge was that I made the mistake of omitting and and or, but it was helpful to include them.
import sys

grade = float(sys.argv[1])
ten = float(grade%1)

if grade > 5:
	print("Enter a Value Between 0 and 5, please")
if grade >= 4.5:
    a = str("A")
elif 3.5 <= grade < 4.5:
    a = str("B")
elif 2.5 <= grade < 3.5:
    a = str("C")
elif 1 <= grade:
    a = str("D")
else:
    a = str("F")

if (grade < 4 and (.85 <= ten and ten < .2)) or (4.7<=grade<4.85) or (1.5<=grade<2):
    b = str(" ")
elif (grade >= 4.85) or ((grade > 2) and (.2 <= ten < .5)) or (2 <= grade < 2.5):
    b = str("+")
elif (.5<= ten < .85) or (grade > 4 and .5 <= ten < .7) or (1<=grade<1.5):
	b = str("-")
else:
	b = str(" ")

if grade <= 5:
	print("Your Grade is:",a,b)