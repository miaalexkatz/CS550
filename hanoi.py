import sys

#-----------------------------------------------------------------------

# Write to standard output instructions to move n Towers of Hanoi
# disks to the left (if parameter left is True) or to the right (if
# parameter left is False).

def moves(n, left):
    print(n)
    if n == 0:
        return
    moves(n-1, not left)
    if left:
        print(str(n) + ' left')
    else:
        print(str(n) + ' right')
    print(n, left)
    moves(n-1, not left)

#-----------------------------------------------------------------------

# Accept integer n as a command-line argument. Write to standard output
# instructions to move n Towers of Hanoi disks to the left.

moves(3, True)


    
#-----------------------------------------------------------------------

# python towersofhanoi.py 1
# 1 left

# python towersofhanoi.py 2
# 1 right
# 2 left
# 1 right

# python towersofhanoi.py 3
# 1 left
# 2 right
# 1 left
# 3 left
# 1 left
# 2 right
# 1 left

# python towersofhanoi.py 4
# 1 right
# 2 left
# 1 right
# 3 right
# 1 right
# 2 left
# 1 right
# 4 left
# 1 right
# 2 left
# 1 right
# 3 right
# 1 right
# 2 left
# 1 right



#Copyright © 2000–2015, Robert Sedgewick, Kevin Wayne, and Robert Dondero. 
#Last updated: Fri Oct 20 20:45:16 EDT 2017.