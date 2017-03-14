#import sys
#print(sys.argv)
"""
Option 2- using any Language, write some code that will receive an integer from a user input. After that, start
a loop that will do the following: if the number is even, split it by 2. if the number is odd, subtract 1 from it.
Keep doing these actions until you reach 0. Return how many split and subtract operations were executed.
"""
def option2():
    #formating console string to allow user to understand what function takes in
    print ("\tBella Lash Option2\n\tThis is a application that takes in an interger and outputs whether the interger is even or odd\n\tIf even will output the number of time it can be divided by 2. If odd will output the number of \n\ttimes it is subtracted by one to react zero.")
    #declaring variable to store count
    i = 0
    #parse string number into interger
    user_int = int(input("\nType in an interger and hit 'Enter'"))
    #if then statement that checks to see if interger is even or odd
    if user_int%2 == 0:
        #if even see how many times the interger can be split by 2
        i = user_int/2
        #formating string to print to console for user
        print ("The interger is %s and it was split by two %d times" % ('even', i))
    #else if that checks to see if odd, could have just used else instead
    elif user_int%2 > 0:
        #loop that keeps subtracting - 1 until it hits 0
        while user_int > 0:
            #subtract one from user's input
            user_int = user_int-1
            #if loop happened increment i
            i = i + 1
        #formating string to print to console for user
        print ("The interger is %s and it was subtracted %d times" % ('odd', i))
#invoking function
option2()
