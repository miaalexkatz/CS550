while True:
    try:
        num = int(input("Pick a Number, 1 to 5 "))
        
        if num>1 and num<5:
            print("thank god")
            break
        else:
        	print("no")
    except ValueError:
        print("That's not valid. Try again. ")
